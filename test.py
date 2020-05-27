import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import random, base64, io


def bmi_calculator(height,weight):
    bmi = weight/height**2
    if bmi < 19:
        return {'bmi': bmi, 'category': 'UnderWeight'}
    elif 19 < bmi < 25:
        return {'bmi': bmi, 'category': 'Healthy Weight'}
    elif 25 <= bmi < 30:
        return {'bmi': bmi, 'category': 'Overweight:Pre-obese'}
    elif 30 <= bmi < 35:
        return {'bmi': bmi, 'category': 'Obese 1'}
    elif 35 <= bmi < 39:
        return {'bmi': bmi, 'category': 'Obese2'}
    else:
        return {'bmi':bmi, 'category': 'Obese3 - Danger'}

def Posture(bmi,score):
    if score < 0.80 and bmi> 35.0:
        return 'Worst'
    elif 0.80 < score < 0.83 and 25.0 < bmi < 30.0:
        return 'Bad'
    elif score > 0.83 and 19.0 < bmi < 25.0:
        return 'Good'
    elif score > 0.90:
        return 'Best'
    else:
        return 'Could be Improved'

def distance_generator(distance, a, b, n):
    distance_temp = np.random.randint(a, b, n).tolist()
    distance.extend(distance_temp)
    return distance


def line_graph(dummy_data):
    plt.figure(figsize=(20, 5))
    fig = sns.lineplot(x='time', y='distance', data=dummy_data, markers='o')
    plt.xlabel('Time (in Hours)')
    plt.ylabel('Average Distance (in CM)')
    plt.xticks(np.arange(0, 10, 1))
    plt.hlines(y=7, xmax=9, xmin=0, linestyles='dashdot', color='red', label='Bad Posture')
    test = fig.get_figure()
    pic_IObytes = io.BytesIO()
    test.savefig(pic_IObytes, format='png')
    pic_hash = base64.b64encode(pic_IObytes.getbuffer()).decode("ascii")
    return pic_hash


def pie_chart(dummy_data):
    fig1, ax1 = plt.subplots()
    ax1.pie(dummy_data.pos.value_counts(normalize=True).to_list(), autopct='%1.1f%%', explode=(0, 0.1),
            labels=['Good/Healthy Posture', 'Bad Posture'])
    test_pie = ax1.get_figure()
    pic_IObytes = io.BytesIO()
    test_pie.savefig(pic_IObytes, format='png')
    pic_hash_pie = base64.b64encode(pic_IObytes.getbuffer()).decode("ascii")
    return pic_hash_pie


def initiate(duration=9):
    val = [(1, 3, 8), (3, 5, 4), (7, 11, 2), (3, 5, 2), (2, 4, 8), (7, 9, 3), (1, 4, 22), (10, 12, 5), (0, 2, 27),
           (7, 9, 5), (0, 3, 23)]
    distance = []
    for i in val:
        distance_generator(distance,a=i[0], b=i[1], n=i[2])
    time = [x for x in range(109)]
    second = random.sample(range(0, 108), 12 * duration)
    data = {'distance': distance, 'time': time}
    dummy_data = pd.DataFrame(data)
    dummy_data = dummy_data.iloc[second]
    dummy_data.time /= 12
    graph_1 = line_graph(dummy_data)
    dummy_data['pos'] = dummy_data.distance < 7
    graph_2 = pie_chart(dummy_data)
    good_per = dummy_data.pos.value_counts(normalize=True)[1]
    return (graph_1, graph_2,good_per)

if __name__ == '__main__':
    print(initiate(9))