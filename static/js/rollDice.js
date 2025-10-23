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

// creates 6 dropdowns (1 for each stat) that lists the roll values
function assignAbilities(rolls) {
    const abilitySelects = document.querySelectorAll(".stat-assigner select");

    // Store remaining available rolls
    let available = [...rolls];

    abilitySelects.forEach(select => {
        populateSelect(select, available);

        select.addEventListener("change", (e) => {
            const prevValue = select.dataset.prevValue ? Number(select.dataset.prevValue) : null;
            const selected = e.target.value ? Number(e.target.value) : null;

            // Restore previous value (if any)
            if (prevValue) {
                available.push(prevValue);
            }

            // Remove only ONE instance of selected value
            if (selected) {
                const idx = available.indexOf(selected);
                if (idx !== -1) available.splice(idx, 1);
            }

            select.dataset.prevValue = selected || "";

            // Repopulate other selects
            abilitySelects.forEach(other => {
                if (other !== select) {
                    const current = other.value ? Number(other.value) : null;
                    populateSelect(other, available.concat(current || []), current);
                }
            });
        });
    });
}


function populateSelect(select, availableValues, currentValue) {
    select.innerHTML = '<option value="">Select value</option>';
    // Clone so sort doesn’t mutate shared array
    [...availableValues].sort((a, b) => b - a).forEach(v => {
        const opt = document.createElement("option");
        opt.value = v;
        opt.textContent = v;
        if (currentValue === v) opt.selected = true;
        select.appendChild(opt);
    });
}