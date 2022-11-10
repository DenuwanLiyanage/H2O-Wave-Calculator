from h2o_wave import Q, main, app, ui
import re

global input_data
input_data = ""


@app('/calc')
async def serve(q: Q):
    global input_data

    if not q.client.initialized:
        q.client.initialized = True

        q.page['head'] = ui.article_card(
            box='1 1 4 2',
            title='Integer Calculator',
            content='This calculator is able to perform basic arithmatic operations on integer values.'
        )

        q.page['input'] = ui.article_card(
            box='1 3 4 1',
            title='',
            content=f'{input_data}'
        )

        q.page['first_Column'] = ui.form_card(
            box='1 4 2 3',
            items=[
                ui.button(
                    name='one',
                    label='1',
                    primary=True,
                ),
                ui.button(
                    name='four',
                    label='4',
                    primary=True,
                ),
                ui.button(
                    name='seven',
                    label='7',
                    primary=True,
                ),
                ui.button(
                    name='plus',
                    label='+',
                    primary=True,
                ),

            ]
        )
        q.page['second_Column'] = ui.form_card(
            box='2 4 2 3',
            items=[
                ui.button(
                    name='two',
                    label='2',
                    primary=True,
                ),
                ui.button(
                    name='five',
                    label='5',
                    primary=True,
                ),
                ui.button(
                    name='eight',
                    label='8',
                    primary=True,
                ),
                ui.button(
                    name='zero',
                    label='0',
                    primary=True,
                ),
            ]
        )
        q.page['third_Column'] = ui.form_card(
            box='3 4 2 3',
            items=[
                ui.button(
                    name='three',
                    label='3',
                    primary=True,
                ),
                ui.button(
                    name='six',
                    label='6',
                    primary=True,
                ),
                ui.button(
                    name='nine',
                    label='9',
                    primary=True,
                ),
                ui.button(
                    name='minus',
                    label='-',
                    primary=True,
                )
            ]
        )

        q.page['fourth_Column'] = ui.form_card(
            box='4 4 1 3',
            items=[
                ui.button(
                    name='clear',
                    label='CL',
                    primary=True,
                ),
                ui.button(
                    name='mul',
                    label='*',
                    primary=True,
                ),
                ui.button(
                    name='dev',
                    label='/',
                    primary=True,
                ),
                ui.button(
                    name='equal',
                    label='=',
                    primary=True,
                )
            ]
        )

    else:

        if q.args.one:
            input_data += str(1)
        if q.args.two:
            input_data += str(2)
        if q.args.three:
            input_data += str(3)
        if q.args.four:
            input_data += str(4)
        if q.args.five:
            input_data += str(5)
        if q.args.six:
            input_data += str(6)
        if q.args.seven:
            input_data += str(7)
        if q.args.eight:
            input_data += str(8)
        if q.args.nine:
            input_data += str(9)
        if q.args.zero:
            input_data += str(0)
        if q.args.plus:
            input_data += '+'
        if q.args.minus:
            input_data += '-'
        if q.args.dev:
            input_data += '/'
        if q.args.mul:
            input_data += '*'
        if q.args.clear:
            input_data = ''
        if q.args.equal:
            value = perform_calculator(input_data)
            input_data = str(value)

        q.page['input'].content = f'{input_data}'

    await q.page.save()


def perform_calculator(input_string):
    data = re.split(r'(\D)', input_string)
    answer = 0

    while '/' in data:
        ind = data.index('/')
        try:
            if int(data[ind+1]) == 0:
                raise ValueError("Divide by Zero")
            val = int(data[ind - 1]) // int(data[ind + 1])
        except ValueError:
            return "Divide Zero"
        data[ind - 1] = val
        del (data[ind])
        del (data[ind])

    for k in data:
        if k == '*':
            ind = data.index('*')
            val = int(data[ind - 1]) * int(data[ind + 1])
            data[ind - 1] = val
            del (data[ind])
            del (data[ind])

    first_no = int(data[0])
    for i in range(1, len(data), 2):
        if data[i] == '+':
            answer = first_no + int(data[i + 1])
        elif data[i] == '-':
            answer = first_no - int(data[i + 1])
        elif data[i] == '/':
            answer = first_no // int(data[i + 1])

        elif data[i] == '*':
            answer = first_no * int(data[i + 1])
        first_no = answer

    return first_no
