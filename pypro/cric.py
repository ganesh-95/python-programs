# to create all sentences using subject verb and object

subjects = raw_input().split(',')
verbs = raw_input().split(',')
objects = raw_input().split(',')

for i in range(len(subjects)):
    for j in range(len(verbs)):
        for k in range(len(objects)):
            print "%s %s %s" % (subjects[i], verbs[j], objects[k])
