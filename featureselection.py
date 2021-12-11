from math import sqrt
import copy


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
                distance = sqrt(distance)  # separate sum pow and sqrt for accuracy

                if distance < nearest_distance:
                    nearest_location = i
                    nearest_distance = distance

        if data[nearest_location][0] == data[k][0]:
            correctly_classified += 1
    # print('correctly_classified' + str(correctly_classified))
    # print('len(data)' + str(len(data)))
    accuracy = (correctly_classified / len(data)) * 100

    return accuracy


def forwardSelection(data):
    current_features = []
    final_features = []  # Init empty subset
    # Init best so far to zero
    best_so_far_accuarcy_final = 0

    # Loop a maximum of num_features times, 2^k - 1 possibilities
    for i in range(1, len(data[0])):
        feature_to_add_final = 0
        feature_to_add_current = 0
        add_to_final_flag = 0
        best_so_far_accuarcy_current = 0

        for j in range(1, len(data[0])):
            if j not in current_features:  # make sure not to compare with itself
                # deep copy for 2d list
                ftmp = copy.deepcopy(current_features)
                # add j to temp current feature set
                ftmp.append(j)
                accuracy = leaveOneOutCrossValidation(data, ftmp)

                # print('     Using feature(s) ' + str(ftmp) + ' accuracy is ' + str(accuracy), '%')
                print(" ".join(["     Using feature(s)", str(ftmp), "accuracy is", str(accuracy), "%"]))

                if accuracy > best_so_far_accuarcy_current:
                    best_so_far_accuarcy_current = accuracy  # update best so far for current set
                    feature_to_add_current = j
                if accuracy > best_so_far_accuarcy_final:
                    best_so_far_accuarcy_final = accuracy  # update best so far for final set
                    feature_to_add_final = j
                    add_to_final_flag = 1

        if add_to_final_flag:
            current_features.append(feature_to_add_final)  # add j to both current and final feature set
            final_features.append(feature_to_add_final)
            # print('\nFeature set ' + str(current_features) + ' was best, accuracy is ' +
            #       str(best_so_far_accuarcy_final) + '%\n')
            print(" ".join(["\nFeature set", str(current_features), "was best, accuracy is", str(best_so_far_accuarcy_final), "%\n"]))
        else:
            current_features.append(feature_to_add_current)  # add j only to current feature set
            # print('\n(Warning, Accuracy has decreased! Continuing search in case of local maxima)' +
            #       '\nFeature set ' + str(current_features) + ' was best, accuracy is '
            #       + str(best_so_far_accuarcy_current) + '%\n')
            print(" ".join(["\n(Warning, Accuracy has decreased! Continuing search in case of local maxima)",
                            "\nFeature set", str(current_features), "was best, accuracy is", str(best_so_far_accuarcy_current),"%\n"]))

    # print('\nFinished search!! The best feature subset is' + str(final_features) +
    #       ' which has an accuracy of ' + str(best_so_far_accuarcy_final) + '%\n')
    print(" ".join(
        ["\nFinished search!! The best feature subset is", str(final_features), "which has an accuracy of", str(best_so_far_accuarcy_final),
         "%\n"]))


def backwardElimination(data, feature, acc):
    current_features = copy.deepcopy(feature)
    final_features = copy.deepcopy(feature)  # copy full feature subset

    # set best so far final accuarcy to k fold accuarcy
    best_so_far_accuarcy_final = 0

    print(" ".join(
        ["\nFeature set", str(current_features), "was best, accuracy is", str(acc), "%\n"]))
    file1 = open("aa.txt", "a")
    file1.write(
        f'\nFeature set {str(current_features)} was best, accuracy is {str(acc)} %\n')
    file1.close()

    # Loop through features
    for i in range(1, len(data[0])-1):
        feature_to_remove_final = -1
        feature_to_remove_current = -1
        remove_to_final_flag = 0
        best_so_far_accuarcy_current = 0

        for j in range(1, len(data[0])):
            if j in current_features:  # different by forward selection, we look for if j is in feature set
                # deep copy for 2d list
                ftmp = copy.deepcopy(current_features)
                # add j to temp current feature set
                ftmp.remove(j)
                accuracy = leaveOneOutCrossValidation(data, ftmp)

                # print('     Using feature(s) ' + str(ftmp) + ' accuracy is ' + str(accuracy), '%')
                print(" ".join(["     Using feature(s)", str(ftmp), "accuracy is", str(accuracy), "%"]))


                # if accuracy > best_so_far_accuarcy_final:
                #     best_so_far_accuarcy_final = accuracy  # update best so far for final set
                #     feature_to_remove_final = j
                #     remove_to_final_flag = 1

                if accuracy > best_so_far_accuarcy_current:
                    best_so_far_accuarcy_current = accuracy  # update best so far for current set
                    feature_to_remove_current = j

        # if remove_to_final_flag:
        current_features.remove(feature_to_remove_current)  # add j to both current and final feature set
        # final_features.remove(feature_to_remove_final)
            # print('\nFeature set ' + str(current_features) + ' was best, accuracy is ' +
            #       str(best_so_far_accuarcy_final) + '%\n')
        print(" ".join(
            ["\nFeature set", str(current_features), "was best, accuracy is", str(best_so_far_accuarcy_current),
            "%\n"]))
        file1 = open("aa.txt", "a")
        file1.write(
            f'\nFeature set {str(current_features)} was best, accuracy is {str(best_so_far_accuarcy_current)} %\n')
        file1.close()
        if best_so_far_accuarcy_current > best_so_far_accuarcy_final:
            # current_features.remove(feature_to_remove_current)  # add j only to current feature set
            # print('\n(Warning, Accuracy has decreased! Continuing search in case of local maxima)' +
            #       '\nFeature set ' + str(current_features) + ' was best, accuracy is '
            #       + str(best_so_far_accuarcy_current) + '%\n')
            best_so_far_accuarcy_final = best_so_far_accuarcy_current
            final_features = current_features.copy()
        else:
            # print(" ".join(["\n(Warning, Accuracy has decreased! Continuing search in case of local maxima)",
            #                 "\nFeature set", str(current_features), "was best, accuracy is",
            #                 str(best_so_far_accuarcy_current), "%\n"]))
            print('(Warning, Accuracy has decreased! Continuing search in case of local maxima)')
            file1 = open("aa.txt", "a")
            # file1.write(
            #     f'\n(Warning, Accuracy has decreased! Continuing search in case of local maxima)\nFeature set {str(current_features)} was best, accuracy is {str(best_so_far_accuarcy_current)} %\n')
            file1.write(f'\n(Warning, Accuracy has decreased! Continuing search in case of local maxima)')
            file1.close()

    # print('\nFinished search!! The best feature subset is' + str(final_features) +
    #       ' which has an accuracy of ' + str(best_so_far_accuarcy_final) + '%\n')
    print(" ".join(
        ["\nFinished search!! The best feature subset is", str(final_features), "which has an accuracy of", str(best_so_far_accuarcy_final),
         "%\n"]))
    file1 = open("aa.txt", "a")
    file1.write(
        f'\nFinished search!! The best feature subset is {str(final_features)} which has an accuracy of {str(best_so_far_accuarcy_final)} %\n')
    file1.close()


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

    # print(num_features) // 10
    # print(num_instances) // 500

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

    # print(instances)
    # print(len(instances)) // num of instance
    # print(len(instances[0]))-1 //num of features
    num_features = len(instances[0]) - 1

    # Algo select
    prompt = input('Type the number of the algorithm you want to run.\n'
                   '  1) Forward Selection\n'
                   '  2) Backward Elimination\n')

    choice = int(prompt)

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
    print('Beginning search.\n')

    if choice == 1:
        forwardSelection(instances)
    elif choice == 2:
        backwardElimination(instances, features, kaccuracy)


if __name__ == '__main__':
    main()
