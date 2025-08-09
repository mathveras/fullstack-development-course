const terminal = document.getElementById("terminal");
    const startBtn = document.getElementById("startBtn");

    function typeWriter(text, speed = 40) {
        return new Promise(resolve => {
            let i = 0;
            function typing() {
                if (i < text.length) {
                    terminal.innerHTML += text.charAt(i);
                    i++;
                    setTimeout(typing, speed);
                } else {
                    terminal.innerHTML += "<br>";
                    resolve();
                }
            }
            typing();
        });
    }

    async function bootSequence() {
        terminal.innerHTML = "";
        await typeWriter("Initializing AI core...");
        await typeWriter("Booting subsystems: [████████████████████████] 100%");
        await typeWriter("Establishing secure uplink...");
        await typeWriter("Connection established.");
        await typeWriter("Awaiting user input...");
        
        const name = prompt("Identify yourself, human:");
        const responses = [
            `Hello ${name}, we've been expecting you. Connecting to N.O.T Soul-SickRat servers.`,
            `User '${name}' detected. Sending requests to Super Definitely S.E.C.R.E.T Army.`,
            `Greetings, ${name}. The prophecy foretold of your arrival.`,
            `Welcome, ${name}. Are you ready to fulfill your destiny?`,
            `Scanning complete. ${name} detected. Confidence level: 3%. Erm...proceeding anyway.`,
            `WARNING: ${name} is now classified as 'suspiciously charming'. Engaging callbacks to avoid softlocking.`
        ];
        const greeting = responses[Math.floor(Math.random() * responses.length)];

        await typeWriter(`Processing...`);
        await typeWriter(greeting);
        await typeWriter(`Processing requested procedures: [█████████████████] 100%`);
        await typeWriter("Protocol complete. Shutting down AI core...");
    }

    startBtn.addEventListener("click", bootSequence);
