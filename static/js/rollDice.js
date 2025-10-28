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
    const available = [...rolls]; // one shared pool of values

    // Remove all existing options & listeners cleanly
    abilitySelects.forEach(select => {
        // Clear previous options
        select.innerHTML = "";
        // Reset any previous state
        select.dataset.prevValue = "";
    });

    // Helper to rebuild all dropdowns based on current available values
    function refreshDropdowns() {
        abilitySelects.forEach(select => {
            const current = select.value ? Number(select.value) : null;
            populateSelect(select, available.concat(current || []), current);
        });
    }

    // Initialize dropdowns
    refreshDropdowns();

    // Add shared event listeners (that all use the same `available` array)
    abilitySelects.forEach(select => {
        // Remove previous listener if re-rolling (clean binding)
        select.onchange = (e) => {
            const prevValue = select.dataset.prevValue ? Number(select.dataset.prevValue) : null;
            const selected = e.target.value ? Number(e.target.value) : null;

            // Restore previously selected value
            if (prevValue !== null) {
                available.push(prevValue);
            }

            // Remove one instance of the newly selected value
            if (selected !== null) {
                const idx = available.indexOf(selected);
                if (idx !== -1) available.splice(idx, 1);
            }

            // Update stored value
            select.dataset.prevValue = selected || "";

            // Refresh dropdowns to reflect updated pool
            refreshDropdowns();
        };
    });
}


function populateSelect(select, availableValues, currentValue) {
    select.innerHTML = '<option value="">Select value</option>';
    [...availableValues].sort((a, b) => b - a).forEach(v => {
        const opt = document.createElement("option");
        opt.value = v;
        opt.textContent = v;
        if (currentValue === v) opt.selected = true;
        select.appendChild(opt);
    });
}
