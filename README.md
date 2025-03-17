# Handwritten-Character-Recognition-with-SQL

## Contents
- Overview
- Features
- How It Works
- Installation & Usage
- Example Execution
- Future Improvements
- License

## Overview
This project implements **Handwriting Recognition** that processes a single drawn character at a time. It utilizes a **Python Canvas** for capturing user input and a **SQL database** for filtering and selecting the best-matching character based on predefined rules.

## Features
- **Single-stroke character recognition** using a graphical drawing interface.
- **Python Tkinter canvas** for capturing handwriting.
- **SQL-based processing** instead of traditional machine learning.
- **Feature extraction** using grid mapping, smoothing, and corner detection.
- **Custom character filtering system** based on the **GRAIL method**.

## How It Works
1. **User draws a character** on the **Python canvas**.
2. **Stroke data is captured** as a sequence of `(x, y)` coordinates.
3. **Coordinates are stored in SQL** using an `INSERT` query.
4. **SQL filtering begins**:
   - The system applies **smoothing** and **thinning** to clean up noise.
   - **Grid mapping** assigns key points to a structured layout.
   - **Feature extraction** detects directional changes and corners.
   - The **best-matching character** is identified using a **criteria-based SQL filter**.
5. **Final result is displayed** as the recognized character.

## Installation & Usage
### Prerequisites
- Python 3
- Tkinter (included in standard Python distributions)
- PostgreSQL or any SQL database that supports `PL/pgSQL`

### Running the Program
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/Handwritten-Character-Recognition-SQL.git
   cd Handwritten-Character-Recognition-SQL
   ```
2. Run the Python canvas:
   ```bash
   python Sescu_Matei_Canvas.py
   ```
3. Draw a character in the canvas window.
4. Copy the generated SQL `INSERT` statement and run it in your SQL database.
5. Execute the SQL recognition query to retrieve the best-matching character.

## Example Execution
### Drawing a Character
A user draws the number **2** on the canvas, which generates SQL output:
```sql
INSERT INTO coords VALUES (0, 174, 106), (1, 174, 110), (2, 174, 116), ...;
```

### SQL Recognition Process
1. **Possible Characters Table** filters candidates based on stroke direction:
   ```sql
   SELECT candidate_characters FROM possible_characters
   WHERE first_four_directions = '{U,R,D,L}';
   ```
2. **Criteria Table** refines selection based on:
   - Start/finish positions
   - Number and positions of corners
   - Aspect ratio
3. **Final SQL Query** retrieves the best match:
   ```sql
   SELECT * FROM character_match ORDER BY total_score DESC LIMIT 1;
   ```

## Future Improvements
- **Visual feedback** to show how recognition is processed step-by-step.
- **Expand dataset** to include more diverse handwriting samples.

## License
This project is free to use and modify for educational purposes.

