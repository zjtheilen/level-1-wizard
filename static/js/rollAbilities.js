// roll 4 dice, drop the lowest, check that it's atleast 8, try again if necessary
// do this seven times, again dropping the lowest grouping
// show the 6 final groups as totals to user, send 6 totalled roll groups to be assigned
function rollAbilities() {
    const rolls = [];

    for (let i = 0; i < 7; i++) {
        let topThreeSum;
        do {
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

// Assign the rolled scores for each stat
// Rolled numbers are removed from selections as they are assigned
function assignAbilities(rolls) {
    const abilitySelects = document.querySelectorAll(".stat-assigner select");
    const available = [...rolls];

    abilitySelects.forEach(select => {
        select.innerHTML = "";
        select.dataset.prevValue = "";
    });

    function refreshDropdowns() {
        abilitySelects.forEach(select => {
            const current = select.value ? Number(select.value) : null;
            populateSelect(select, available.concat(current || []), current);
        });
    }

    refreshDropdowns();

    abilitySelects.forEach(select => {
        select.onchange = (e) => {
            const prevValue = select.dataset.prevValue ? Number(select.dataset.prevValue) : null;
            const selected = e.target.value ? Number(e.target.value) : null;

            if (prevValue !== null) {
                available.push(prevValue);
            }

            if (selected !== null) {
                const idx = available.indexOf(selected);
                if (idx !== -1) available.splice(idx, 1);
            }

            select.dataset.prevValue = selected || "";

            refreshDropdowns();
        };
    });
}

// Display rolled numbers from rollAbilities() as options in dropdown menus for each stat
function populateSelect(select, availableValues, currentValue) {
    select.innerHTML = '<option value="">Select</option>';
    [...availableValues].sort((a, b) => b - a).forEach(v => {
        const opt = document.createElement("option");
        opt.value = v;
        opt.textContent = v;
        if (currentValue === v) opt.selected = true;
        select.appendChild(opt);
    });
}
