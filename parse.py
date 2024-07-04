import pandas as pd
import numpy as np

auditLogDF = pd.read_csv(r"audit-logs.csv", names=['hostIP', 'Timestamp', 'username', 'verb', 'resourceType', 'subresource', 'ObjectName', 'ObjectName1', 'requestURI', 'auditID', 'stage', 'statusCode', 'UID', 'ReferenceUID', 'UID1'])


#print(auditLogDF.count)
# auditLogDF = auditLogDF.drop_duplicates()
#print(auditLogDF.count)
auditLogDF = auditLogDF.drop(auditLogDF.columns[[0, 2, 5, 8, 9, 10, 11]], axis=1)
auditLogDF = auditLogDF[auditLogDF.verb != "get"]
auditLogDF = auditLogDF[auditLogDF.verb != "watch"]
auditLogDF = auditLogDF[auditLogDF.verb != "list"]
auditLogDF = auditLogDF[auditLogDF.resourceType != "events"]
auditLogDF = auditLogDF[auditLogDF.resourceType != "leases"]

#print(auditLogDF.count)
auditLogDF = auditLogDF[auditLogDF.resourceType != "replicationcontrollers"]

auditLogDF["event_type"] = auditLogDF["verb"] + "_" + auditLogDF["resourceType"]
#auditLogDF = auditLogDF[auditLogDF.event_type != "delete_service"]
#auditLogDF = auditLogDF[auditLogDF.event_type != "create namespaces"]
auditLogDF['ObjectName'] = auditLogDF['ObjectName'].combine_first(auditLogDF['ObjectName1'])
auditLogDF["UID"] = auditLogDF["UID"].fillna(auditLogDF['UID1'])
auditLogDF = auditLogDF.drop(auditLogDF.columns[[4, 7]], axis=1)
auditLogDF["UID"] = auditLogDF["ReferenceUID"].fillna(auditLogDF['UID'])
#auditLogDF = auditLogDF.sort_values(["UID", "Timestamp"], ascending = (False, True))
auditLogDF = auditLogDF.drop(auditLogDF.columns[[0, 5]], axis=1)
#auditLogDF = auditLogDF.drop_duplicates()

#print(auditLogDF.to_string())
#print(auditLogDF.count)
print(auditLogDF)


event_seq = []
event_sub_seq = []
for c, r in auditLogDF.iterrows():
    with open("events-dataset.txt", "a") as event_file:
        event_file.write("%s\n" % r['event_type'])