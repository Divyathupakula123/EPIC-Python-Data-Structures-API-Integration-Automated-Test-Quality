# Day 1 - Data Structures and Complexity

## Objective
Build a Python utility to process records and remove duplicate IDs.

## Technologies
- Python
- Lists
- Sets
- Pytest
- Git

## Implementation
The get_unique_ids() function accepts a list of records.
It uses a set to track IDs already seen and a list to
preserve the original order of unique IDs.

## Complexity Analysis
Let n be the number of records.

- Time Complexity: O(n) average
- Auxiliary Space Complexity: O(n)

The set provides average O(1) membership checks.
The list preserves the order of unique IDs.

## How to Run
Run the tests with:

python -m pytest -v

## Test Coverage
- Duplicate IDs
- Empty input
- Original order preservation
- Missing ID error

## Known Limitations
- Each record must be a dictionary.
- Each record must contain an "id" key.
- IDs must be hashable for set membership.

## Result
The utility removes duplicate IDs while preserving order.
## Data Structures Comparison

| Data Structure | Purpose | Average Time | Space |
|---|---|---|---|
| List | Store records in order | O(1) append | O(n) |
| Dictionary | Find records by ID | O(1) lookup | O(n) |
| Set | Store unique IDs | O(1) add/check | O(n) |
| Queue | Process records FIFO | O(1) remove from front | O(n) |

## Complexity Notes

For n records:
- List creation takes O(n) time and O(n) space.
- Dictionary creation takes O(n) average time and O(n) space.
- Set creation takes O(n) average time and O(n) space.
- Queue processing takes O(n) time and O(n) space.

Dictionary and set operations are O(1) on average,
but can be O(n) in worst-case collision scenarios.

## Known Limitations

- Every record must contain an ID.
- IDs must be hashable.
- Duplicate dictionary IDs overwrite earlier records.