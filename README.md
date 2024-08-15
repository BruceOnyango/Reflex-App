# Reflex-App
# Installation and Setup for Reflex

1. **Create a virtual environment** (recommended, but not necessary):
    ```bash
    python -m venv .venv
    ```

2. **Activate your virtual environment**:
    - **On Windows**:
      ```bash
      .\.venv\Scripts\activate
      ```
    - **On macOS/Linux**:
      ```bash
      source .venv/bin/activate
      ```

3. **Upgrade pip** (not necessary but might reduce setup issues):
    ```bash
    pip install --upgrade pip
    ```

4. **Use the `requirements.txt` to install the packages**:
    ```bash
    pip install -r requirements.txt
    ```

5. **Initialize the Reflex database**:
    ```bash
    reflex db init
    ```

6. **Make modifications to `alembic.ini`**:
    - Point `sqlalchemy.url` to your URL `driver://user:pass@localhost/dbname` and change it to your specific case.

7. **Create migrations**:
    ```bash
    reflex db makemigrations --message 'something changed'
    ```

8. **Apply migrations**:
    ```bash
    reflex db migrate
    ```

9. **Run Reflex**:
    ```bash
    reflex run
    ```
