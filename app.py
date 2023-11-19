from flask import Flask, render_template
import pandas as pd
import plotly.express as px

app = Flask(__name__)
# Datos de ejemplo (para fines ilustrativos)
df = pd.DataFrame({'X': [1, 2, 3, 4, 5], 'Y': [10, 11, 12, 13, 14]})

@app.route('/')
def index():
    fig = px.bar(df, x='X', y='Y', title='Gráfico de Dispersión Interactivo', labels={'X': 'Eje X', 'Y': 'Eje Y'})
    return render_template('index.html', plot=fig.to_html())

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False)
