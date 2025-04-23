from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# ✅ Load CSV file
df = pd.read_csv('glo.csv')  # Make sure 'glo.csv' is in the same folder as app.py
print("CSV loaded successfully:")
print(df.head())

@app.route('/', methods=['GET', 'POST'])
def index():
    results = None
    query = ''
    if request.method == 'POST':
        query = request.form['search'].lower().strip()
        filtered_df = df[df.apply(lambda row: row.astype(str).str.lower().str.contains(query).any(), axis=1)]
        results = filtered_df.to_dict(orient='records')
        print("Filtered results:")
        print(results)

    return render_template('index.html', results=results, query=query)

if __name__ == '__main__':
    app.run(debug=True)
