# Decision_Tree

🌲 Manual Decision Tree Classifier (ID3)
I built this script to show how a Decision Tree actually thinks. Instead of just using scikit-learn to do the heavy lifting, I wrote the logic to calculate Entropy and Information Gain manually to see how the algorithm picks the best features from a dataset.

## 📊 Dataset

- **Samples:** 14
- **Features:** 4
  - A (Binary)
  - B (Binary)
  - C (3 values)
  - D (3 values)
- **Target Classes:**
  - Healthy
  - Sick

*(The full table is based on the image provided in this repo)*


## 🧠 How it works
The code follows the **ID3 Algorithm** step-by-step:

1. **Root Entropy**: It checks how mixed the "Sick vs Healthy" data is at the very beginning.
2. **Finding the Best Feature**: The script loops through A, B, C, and D to see which one clears up the most confusion (Information Gain).
3. **Branching**:
   - For this specific data, **Feature D** was chosen as the best starting point (the root).
   - The script then splits into sub-layers to finish the tree.

> **Note:** I used `numpy` only for the `log2` math. Everything else is logic based on counting the table rows.

---

##  The Final Tree Result
After running the math for all layers, this is the most efficient tree structure:

```text
          [ Feature D ]
         /      |      \
     D=1       D=2       D=3
      |         |         |
 [ Feature B ] [ SICK ] [ Feature A ]
    /    \                 /    \
  B=0    B=1             A=0    A=1
   |      |               |      |
[SICK] [HEALTHY]       [SICK] [HEALTHY]
