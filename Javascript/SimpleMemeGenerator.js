/**
 * SimpleMemeGenerator: Generates a random meme caption by combining predefined top and bottom texts.
 *
 * This function simulates a "meme" by outputting text in a classic meme format.
 */
function generateRandomMemeCaption() {
    // --- Data: Lists of common meme text components ---
    const TOP_TEXTS = [
        "One does not simply",
        "Brace yourselves,",
        "You had one job.",
        "They asked me what I do.",
        "Wait, that's illegal.",
        "A challenger appears."
    ];

    const BOTTOM_TEXTS = [
        "understand this code.",
        "the JavaScript is coming.",
        "and you failed it.",
        "I said I write code.",
        "I will ignore that.",
        "The bug won't fix itself."
    ];

    // --- Random Selection Logic ---

    /**
     * Helper function to get a random item from an array.
     */
    function getRandomItem(arr) {
        // Math.random() returns a float between 0 (inclusive) and 1 (exclusive).
        // Multiplying by arr.length gives a number between 0 and arr.length.
        // Math.floor() converts it to a solid integer index.
        const randomIndex = Math.floor(Math.random() * arr.length);
        return arr[randomIndex];
    }

    // 1. Get a random top text
    const topText = getRandomItem(TOP_TEXTS);

    // 2. Get a random bottom text
    const bottomText = getRandomItem(BOTTOM_TEXTS);

    // 3. Combine them into a classic meme format
    return `
🔥 RANDOM MEME CAPTION 🔥

--- TOP TEXT ---
${topText.toUpperCase()}

--- BOTTOM TEXT ---
${bottomText.toUpperCase()}
    `;
}

// --- Example Usage ---

console.log(generateRandomMemeCaption());
console.log("\n" + "=".repeat(40) + "\n");
console.log(generateRandomMemeCaption());