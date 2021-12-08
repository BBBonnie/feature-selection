
# This function is from the psuedo-code in slides provided by Prof. Keogh
def leaveOneOutCrossValidation(data, features):
    correctly_classified = 0
    for k in range(len(data)):  # loop instances
        # object_to_classify = data[i][1:]
        # label = data[i][0]

        nearest_distance = float('inf')  # track nearest neighbor distance
        nearest_location = 0  # track nearest neighbor location

        for i in range(len(data)):  # loop instances
            if k == i:
                pass
            else:
                distance = 0  # reset distance
                for j in range(len(features)):  # go through feature set
                    distance += pow((data[i][features[j]] - data[k][features[j]]), 2)
                distance = math.sqrt(distance)  # separate sum pow and sqrt for accuracy

                if distance < nearest_distance:
                    nearest_location = i
                    nearest_distance = distance

        if data[nearest_location][0] == data[k][0]:
            correctly_classified += 1
    print('correctly_classified' + str(correctly_classified))
    print('len(data)' + str(len(data)))
    accuracy = (correctly_classified / len(data)) * 100

    return accuracy
  
  def main():
    global instances
    print('---------- Feature Selection ----------\n')
    file_name = input('Type in the name of the file to test: ')

    # reference: https://stackoverflow.com/questions/29591968/python-list-of-floats-from-text-file
    try:
        rawdata = open(file_name, 'r')
    except:
        raise IOError(file_name + ' does not exist. Exit...')

    # count number of instances
    cnt = 0
    for r in rawdata:
        cnt += 1
    num_instances = cnt

    print(num_features) // 10
    print(num_instances) // 500

    # Use seek(0) to reset cursor to start of file
    # https://www.tutorialspoint.com/python/file_seek.htm
    rawdata.seek(0, 0)

    # init a 2d instance list of number of instances rows
    instances = [0] * num_instances
    for i in range(num_instances):
        # fill in each row with split data from file
        # reference: https://stackoverflow.com/questions/29591968/python-list-of-floats-from-text-file
        instances[i] = [float(j) for j in rawdata.readline().split()]

    rawdata.close()  # close file

    print(instances)
    print(len(instances)) // num of instance
    print(len(instances[0]))-1 //num of features
    num_features = len(instances[0]) - 1

    print('This dataset has ' + str(num_features) +
          ' features (not including the class attribute), with ' +
          str(num_instances) + ' instances.')

    # append all features in a list
    features = []
    for ft in range(1, len(instances[0])):
        features.append(ft)
    # k fold with all features
    kaccuracy = leaveOneOutCrossValidation(instances, features)

    print('Running nearest neighbor with all ' + str(num_features) +
          ' features, using "leaving-one-out" evaluation, I get an accuracy of ' + str(kaccuracy), '%\n')
