# Decision_Tree

🌲 Manual Decision Tree Classifier (ID3)
I built this script to show how a Decision Tree actually thinks. Instead of just using scikit-learn to do the heavy lifting, I wrote the logic to calculate Entropy and Information Gain manually to see how the algorithm picks the best features from a dataset.

📊 The Dataset
The data is based on a medical table (included in the repo image) where we try to predict if someone is Sick or Healthy based on four features: A, B, C, and D.
Feature	Description
A	Binary (0 or 1)
B	Binary (0 or 1)
C	Categories (1, 2, 3)
D	Categories (1, 2, 3)

🧠 How it works
The code follows the ID3 Algorithm step-by-step:
Entropy Check: It calculates the initial "messiness" (Entropy) of the whole group.
Split Calculation: It loops through features A, B, C, and D to see which one reduces that messiness the most (highest Information Gain).
Branching: Once it finds the best feature (spoiler: it's D), it splits the data and repeats the process for the sub-groups until it reaches a clear "Sick" or "Healthy" conclusion.
Note: I used numpy for the log2 math, but everything else is pure logic based on the frequency of occurrences in the table.

🏗️ The Resulting Tree
After running the calculations for all layers, the "perfect" tree for this dataset looks like this:
code
Mermaid
graph TD
    Root((Feature D))
    
    Root -- D=1 --> B_Node[Feature B]
    Root -- D=2 --> Sick1[Final: Sick]
    Root -- D=3 --> A_Node[Feature A]

    B_Node -- B=0 --> Sick2[Final: Sick]
    B_Node -- B=1 --> Healthy1[Final: Healthy]

    A_Node -- A=0 --> Sick3[Final: Sick]
    A_Node -- A=1 --> Healthy2[Final: Healthy]
    
    style Sick1 fill:#f96,stroke:#333
    style Sick2 fill:#f96,stroke:#333
    style Sick3 fill:#f96,stroke:#333
    style Healthy1 fill:#6f9,stroke:#333
    style Healthy2 fill:#6f9,stroke:#333
