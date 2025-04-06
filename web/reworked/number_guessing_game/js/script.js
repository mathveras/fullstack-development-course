/** 
 * A simple Number Guessing Game game where the player tries to guess a randomly generated number. 
 */

// Game configuration
const config = {
  difficulties: {
    easy: { min: 1, max: 10, attempts: 10, points: 10 },
    medium: { min: 1, max: 50, attempts: 8, points: 30 },
    hard: { min: 1, max: 100, attempts: 6, points: 50 }
  },
  // Sound effects
  sounds: {
    win: 'sounds/mixkit-correct-answer-reward-952.wav',
    lose: 'sounds/mixkit-wrong-answer-fail-notification-946.wav',
    wrong: 'sounds/mixkit-tech-break-fail-2947.wav',
    click: 'sounds/mixkit-click-error-1110.wav'
  }
};

// Game state
const gameState = {
  randomNumber: null,
  attemptsLeft: 0,
  score: 0,
  highScore: localStorage.getItem('highScore') || 0,
  currentDifficulty: 'easy',
  guesses: [],
  minRange: 1,
  maxRange: 10,
  gameOver: false,
  soundEnabled: localStorage.getItem('soundEnabled') !== 'false'
};

// DOM Elements
const elements = {
  difficultySelect: document.getElementById('difficulty'),
  guessInput: document.getElementById('guess-input'),
  guessButton: document.getElementById('guess-button'),
  newGameButton: document.getElementById('new-game'),
  rangeText: document.getElementById('range'),
  maxAttemptsText: document.getElementById('max-attempts'),
  attemptsText: document.getElementById('attempts'),
  previousGuesses: document.getElementById('previous-guesses'),
  resultMessage: document.getElementById('result-message'),
  hintMarker: document.getElementById('hint-marker'),
  hintContainer: document.getElementById('hint-container'),
  scoreDisplay: document.getElementById('score'),
  highScoreDisplay: document.getElementById('highscore'),
  modal: document.getElementById('modal'),
  modalTitle: document.getElementById('modal-title'),
  modalMessage: document.getElementById('modal-message'),
  modalClose: document.getElementById('modal-close'),
  resetRecordButton: document.getElementById('reset-record')
};

// Audio objects for sound effects
const audio = {};
for (const [key, url] of Object.entries(config.sounds)) {
  audio[key] = new Audio(url);
}

/**
 * Initialize the game
 */
function initGame() {
  // Load high score from local storage
  updateScoreDisplay();
  
  // Set up event listeners
  elements.difficultySelect.addEventListener('change', handleDifficultyChange);
  elements.guessButton.addEventListener('click', handleGuess);
  elements.guessInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') {
      handleGuess();
    }
  });
  elements.newGameButton.addEventListener('click', startNewGame);
  elements.modalClose.addEventListener('click', closeModal);
  elements.resetRecordButton.addEventListener('click', resetHighScore);
  
  // Start a new game
  startNewGame();
}

/**
 * Start a new game
 */
function startNewGame() {
  const difficulty = config.difficulties[gameState.currentDifficulty];
  
  // Reset game state
  gameState.attemptsLeft = difficulty.attempts;
  gameState.guesses = [];
  gameState.gameOver = false;
  gameState.minRange = difficulty.min;
  gameState.maxRange = difficulty.max;
  
  // Generate random number
  gameState.randomNumber = Math.floor(Math.random() * (difficulty.max - difficulty.min + 1)) + difficulty.min;
  
  // Reset UI
  elements.guessInput.value = '';
  elements.guessInput.min = difficulty.min;
  elements.guessInput.max = difficulty.max;
  elements.guessInput.disabled = false;
  elements.guessButton.disabled = false;
  elements.previousGuesses.textContent = '';
  elements.resultMessage.textContent = '';
  elements.resultMessage.className = 'result-message';
  elements.newGameButton.classList.add('hidden');
  elements.rangeText.textContent = `${difficulty.min} e ${difficulty.max}`;
  elements.maxAttemptsText.textContent = difficulty.attempts;
  elements.attemptsText.textContent = difficulty.attempts;
  
  // Reset hint bar
  resetHintMarker();
  
  // Focus input
  elements.guessInput.focus();
  
  console.log('New game started. Random number:', gameState.randomNumber);
}

/**
 * Handle difficulty change
 */
function handleDifficultyChange() {
  gameState.currentDifficulty = elements.difficultySelect.value;
  startNewGame();
}

/**
 * Handle player guess
 */
function handleGuess() {
  if (gameState.gameOver) return;
  
  const userGuess = parseInt(elements.guessInput.value);
  const difficulty = config.difficulties[gameState.currentDifficulty];
  
  // Validate input - only check against the difficulty range, not the adjusted ranges
  if (isNaN(userGuess) || userGuess < difficulty.min || userGuess > difficulty.max) {
    elements.guessInput.classList.add('shake');
    setTimeout(() => elements.guessInput.classList.remove('shake'), 500);
    playSound('click');
    return;
  }
  
  // Check if the guess has already been made
  if (gameState.guesses.includes(userGuess)) {
    elements.resultMessage.textContent = `You already tried ${userGuess}! Try another number.`;
    elements.resultMessage.classList.add('shake');
    setTimeout(() => elements.resultMessage.classList.remove('shake'), 500);
    elements.guessInput.value = '';
    elements.guessInput.focus();
    playSound('click');
    return;
  }
  
  // Clear input field
  elements.guessInput.value = '';
  elements.guessInput.focus();
  
  // Update attempts left
  gameState.attemptsLeft--;
  elements.attemptsText.textContent = gameState.attemptsLeft;
  
  // Add to previous guesses
  gameState.guesses.push(userGuess);
  updatePreviousGuesses();
  
  // Check if guess is correct
  if (userGuess === gameState.randomNumber) {
    handleCorrectGuess();
  } else if (gameState.attemptsLeft === 0) {
    handleGameOver();
  } else {
    handleWrongGuess(userGuess);
  }
}

/**
 * Handle correct guess
 */
function handleCorrectGuess() {
  // Calculate score based on difficulty and attempts left
  const difficultyConfig = config.difficulties[gameState.currentDifficulty];
  const basePoints = difficultyConfig.points;
  const attemptsBonus = gameState.attemptsLeft * 5;
  const pointsEarned = basePoints + attemptsBonus;
  
  // Update score and high score
  gameState.score += pointsEarned;
  if (gameState.score > gameState.highScore) {
    gameState.highScore = gameState.score;
    localStorage.setItem('highScore', gameState.highScore);
  }
  updateScoreDisplay();
  
  // Update UI
  elements.resultMessage.textContent = `That's right! You won!`;
  elements.resultMessage.classList.add('success', 'pulse');
  elements.guessInput.disabled = true;
  elements.guessButton.disabled = true;
  elements.newGameButton.classList.remove('hidden');
  gameState.gameOver = true;
  
  // Position hint marker
  updateHintMarker(gameState.randomNumber);
  
  // Play sound
  playSound('win');
  
  // Show modal
  showModal(
    'Victory!', 
    `You guessed the correct number ${gameState.randomNumber} with ${difficultyConfig.attempts - gameState.attemptsLeft} attempts!
     Earned ${pointsEarned} points.`
  );
}

/**
 * Handle game over (no more attempts)
 */
function handleGameOver() {
  // Update UI
  elements.resultMessage.textContent = `No more attemps! The correct number was: ${gameState.randomNumber}.`;
  elements.resultMessage.classList.add('error');
  elements.guessInput.disabled = true;
  elements.guessButton.disabled = true;
  elements.newGameButton.classList.remove('hidden');
  gameState.gameOver = true;
  
  // Position hint marker at correct number
  updateHintMarker(gameState.randomNumber);
  
  // Play sound
  playSound('lose');
  
  // Show modal
  showModal(
    'Game Over!', 
    `Your attempts are over. The correct number was ${gameState.randomNumber}.
     Try again with a new game!`
  );
}

/**
 * Handle wrong guess
 * @param {number} userGuess - The player's guess
 */
function handleWrongGuess(userGuess) {
  // Update hint text without restricting input range
  if (userGuess < gameState.randomNumber) {
    elements.resultMessage.textContent = 'Too low! Try a higher number.';
    // The next line is commented out to not restrict input range
    // gameState.minRange = Math.max(gameState.minRange, userGuess + 1);
  } else {
    elements.resultMessage.textContent = 'Too high! Try a lower number.';
    // The next line is commented out to not restrict input range
    // gameState.maxRange = Math.min(gameState.maxRange, userGuess - 1);
  }
  
  // Update hint marker
  updateHintMarker(userGuess);
  
  // Play sound
  playSound('wrong');
}

/**
 * Update the display of previous guesses
 */
function updatePreviousGuesses() {
  elements.previousGuesses.textContent = `Previous guesses: ${gameState.guesses.join(', ')}`;
}

/**
 * Update the score display
 */
function updateScoreDisplay() {
  elements.scoreDisplay.textContent = gameState.score;
  elements.highScoreDisplay.textContent = gameState.highScore;
}

/**
 * Reset the hint marker position
 */
function resetHintMarker() {
  elements.hintMarker.style.left = '50%';
}

/**
 * Update the hint marker position based on the guess
 * @param {number} guess - The player's guess
 */
function updateHintMarker(guess) {
  const { min, max } = config.difficulties[gameState.currentDifficulty];
  const range = max - min;
  const position = ((guess - min) / range) * 100;
  elements.hintMarker.style.left = `${position}%`;
}

/**
 * Play a sound effect
 * @param {string} soundName - The name of the sound to play
 */
function playSound(soundName) {
  if (!gameState.soundEnabled || !audio[soundName]) return;
  
  // Stop the sound if it's already playing
  audio[soundName].pause();
  audio[soundName].currentTime = 0;
  
  // Play the sound
  audio[soundName].play().catch(e => console.error('Error playing sound:', e));
}

/**
 * Show modal with custom message
 * @param {string} title - Modal title
 * @param {string} message - Modal message
 * @param {boolean} useConfirmationButtons - Whether to use confirmation buttons instead of the default
 */
function showModal(title, message, useConfirmationButtons = false) {
  elements.modalTitle.textContent = title;
  elements.modalMessage.textContent = message;
  
  // Check if we need to restore the default button
  const modalContent = elements.modal.querySelector('.modal-content');
  const hasFooter = modalContent.querySelector('.modal-footer');
  
  if (!useConfirmationButtons && hasFooter) {
    // Restore the default button
    const modalFooter = modalContent.querySelector('.modal-footer');
    const defaultButton = document.createElement('button');
    defaultButton.id = 'modal-close';
    defaultButton.textContent = 'Ok!';
    defaultButton.addEventListener('click', closeModal);
    
    // Replace footer with default button
    modalContent.replaceChild(defaultButton, modalFooter);
    elements.modalClose = defaultButton;
  }
  
  elements.modal.classList.add('show');
}

/**
 * Close the modal
 */
function closeModal() {
  elements.modal.classList.remove('show');
}

/**
 * Reset high score by clearing localStorage
 */
function resetHighScore() {
  // Show confirmation modal with custom buttons
  showModal(
    'Reset Record',
    'Are you sure you want to clear your record? This action cannot be undone.',
    true // Use confirmation buttons
  );
  
  // Replace the default modal close button with confirm/cancel buttons
  const modalContent = elements.modal.querySelector('.modal-content');
  const modalFooter = document.createElement('div');
  modalFooter.className = 'modal-footer';
  
  const confirmButton = document.createElement('button');
  confirmButton.textContent = 'Confirm';
  confirmButton.className = 'confirm-button';
  confirmButton.addEventListener('click', () => {
    // Clear high score from localStorage
    localStorage.removeItem('highScore');
    
    // Reset game state
    gameState.highScore = 0;
    gameState.score = 0;
    
    // Update display
    updateScoreDisplay();
    
    // Show success message with default button
    showModal('Record Reset', 'Your record has been cleared successfully!');
    
    // Play sound
    playSound('click');
  });
  
  const cancelButton = document.createElement('button');
  cancelButton.textContent = 'Cancel';
  cancelButton.className = 'cancel-button';
  cancelButton.addEventListener('click', closeModal);
  
  modalFooter.appendChild(cancelButton);
  modalFooter.appendChild(confirmButton);
  
  // Find and replace the default button
  const defaultButton = modalContent.querySelector('#modal-close');
  if (defaultButton) {
    modalContent.replaceChild(modalFooter, defaultButton);
  } else {
    // If no default button (already replaced), just replace the footer
    const oldFooter = modalContent.querySelector('.modal-footer');
    if (oldFooter) {
      modalContent.replaceChild(modalFooter, oldFooter);
    } else {
      modalContent.appendChild(modalFooter);
    }
  }
}

// Initialize the game when DOM is loaded
document.addEventListener('DOMContentLoaded', initGame); 