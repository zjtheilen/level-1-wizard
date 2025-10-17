function rollAbilities() {
    let final_scores = []
    for (let i = 0; i < 7; i++) {
        let results = [];
        let topThreeSum = 0;
        do {
            results = [];
            for (let i = 0; i < 4; i++) {
                results.push(Math.floor(Math.random() * 6) + 1);
            }
            const sorted = [...results].sort((a, b) => b - a);
            topThreeSum = sorted.slice(0, 3).reduce((a, b) => a + b, 0);
        } while (topThreeSum < 8);
        final_scores.push(topThreeSum)
    }
    const smallestIndex = final_scores.indexOf(Math.min(...final_scores));
    if (smallestIndex !== -1) {
        final_scores.splice(smallestIndex, 1);
    }
    document.getElementById("roleScores").innerText = final_scores
}