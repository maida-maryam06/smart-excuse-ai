import pandas as pd
import os

FEEDBACK_FILE = "dataset/user_feedback.csv"


def save_feedback(excuse, label):

    new_row = pd.DataFrame({
        "excuse":[excuse],
        "label":[label]
    })

    if os.path.exists(FEEDBACK_FILE):

        df = pd.read_csv(FEEDBACK_FILE)

        df = pd.concat([df,new_row], ignore_index=True)

    else:

        df = new_row

    df.to_csv(FEEDBACK_FILE, index=False)