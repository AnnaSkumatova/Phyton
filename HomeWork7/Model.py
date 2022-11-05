m_data =''
result = 0
prioritet = ['*', '/', '+','-']

def set_math(data:str):
    global m_data
    m_data = data


def Get_math():
    global m_data
    return m_data

def set_result(m_data: str):
    global result
    list_Result = m_data.replace(" ","")
    list_Result = list_Result.replace("+", " + ").replace("-"," - ").replace("*"," * ").replace('/',' / ')
    list_Result = list_Result.split(' ')
    while len(list_Result)>1:
        if prioritet[0] in list_Result or prioritet[1] in list_Result:
            for i in range(1, len(list_Result)-1):
                if list_Result[i] == prioritet[0]:
                    list_Result[i-1] = int(list_Result[i-1])*int(list_Result[i+1])
                    break

                elif list_Result[i] == prioritet[1]:
                    list_Result[i-1] = int(list_Result[i-1])/int(list_Result[i+1])
                    break
        else:
            for i in range(1, len(list_Result)-1):

                if list_Result[i] == prioritet[2]:
                    list_Result[i-1] = int(list_Result[i-1])+int(list_Result[i+1])
                    break
                elif list_Result[i] == prioritet[3]:
                    list_Result[i-1] = int(list_Result[i-1])-int(list_Result[i+1])
                    break
        list_Result.pop(i)
        list_Result.pop(i)

    result = list_Result

    return result

def get_result():
    global result
    return result