function countSwaps(a) {
    let i, j, temp;
    let swaps = 0;
    const n = a.length;
    for (i = 0; i < n; i++) {

        for (j = 0; j < n - 1; j++) {
            // Swap adjacent elements if they are in decreasing order
            if (a[j] > a[j + 1]) {
                temp = a[j];
                a[j] = a[j + 1];
                a[j + 1] = temp;
                swaps = swaps + 1;
            }
        }

    }
    console.log(`Array is sorted in ${swaps} swaps.`)
    console.log(`First Element: ${a[0]}`);
    console.log(`Last Element: ${a[a.length - 1]}`);
}

countSwaps([1, 2, 3, 4]);
console.log('---');
countSwaps([4, 2, 3, 1]);
