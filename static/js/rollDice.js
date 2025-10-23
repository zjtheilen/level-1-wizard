function rollAbilities() {
    const rolls = [];

    // roll 7 times and drop the lowest (keeping 6)
    for (let i = 0; i < 7; i++) {
        let topThreeSum;
        // do / while -> make sure all stats are no less than 8
        do {
            // roll 4d6 and drop the lowest (keeping 3d6)
            const dice = Array.from({ length: 4 }, () => Math.floor(Math.random() * 6) + 1);
            const sorted = dice.sort((a, b) => b - a);
            topThreeSum = sorted.slice(0, 3).reduce((a, b) => a + b, 0);
        } while (topThreeSum < 8);

        rolls.push(topThreeSum)
    }
    const smallestIndex = rolls.indexOf(Math.min(...rolls));
    if (smallestIndex !== -1) {
        rolls.splice(smallestIndex, 1);
    }
    document.getElementById("roleScores").innerText = rolls.join(", ")

    assignAbilities(rolls)
}

// currently doing nothing - > will allow users to assign the rolled stats
// creates 6 dropdowns (1 for each stat) that lists the roll values
function assignAbilities(rolls) {
    const abilitySelects = document.querySelectorAll(".stat-assigner select");
    abilitySelects.forEach(select => {
        select.innerHTML = '<option value="">Select value</option>';
        rolls.forEach((r, idx)=> {
            const opt = document.createElement("option");
            opt.value = r;
            opt.innerText = r;
            select.appendChild(opt)
        });
    });

    window.rolledAbilities = rolls;
}