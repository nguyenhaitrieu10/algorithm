import helper
import postfix
import sort
import topology

def test_sort(sort_func=sort.flash_sort, a = None, num_sample = 20):
    if not a:
        a = helper.init_arr(length=num_sample)

    print("----------Array----------")
    print(a)
    sort_func(a)
    print("-------Sorted Array------")
    print(a)
    print(helper.check_order(a))


def test_postfix(s="  5.5  /2 + 3*(4/8 -2)  ", expected_result=-1.75):
    print("-----------Input-----------")
    print(s)
    result = postfix.calculate(s)
    print("-----------Result-----------")
    print(result)
    print("-------Expected Result-------")
    print(expected_result)

LIST_OF_RECORDS = [{'STT':1,'ID':'now-express-api','Label':'now-express-api','Depend':'','Time':'09:00','Note':'expecttofail2smoketests'},{'STT':2,'ID':'now-express-cron','Label':'now-express-cron','Depend':'','Time':'09:00','Note':''},{'STT':3,'ID':'now-express-admin-api','Label':'now-express-admin-api','Depend':'','Time':'09:00','Note':''},{'STT':4,'ID':'now-express-admin-cron','Label':'now-express-admin-cron','Depend':'','Time':'09:30','Note':''},{'STT':5,'ID':'now-admin-api','Label':'now-admin-api','Depend':'api-service,promotion-service,nowaccount-api','Time':'09:30','Note':''},{'STT':6,'ID':'now-admin-cron','Label':'now-admin-cron','Depend':'now-admin-api','Time':'09:00','Note':''},{'STT':7,'ID':'api-service','Label':'api-service','Depend':'','Time':'09:00','Note':''},{'STT':8,'ID':'nowmenu-api','Label':'nowmenu-api','Depend':'','Time':'09:00','Note':''},{'STT':9,'ID':'nowmerchant-cron','Label':'nowmerchant-cron','Depend':'api-service','Time':'09:00','Note':''},{'STT':10,'ID':'nowmerchant-api','Label':'nowmerchant-api','Depend':'api-service,nowmenu-api','Time':'09:00','Note':''},{'STT':11,'ID':'nowexternal-api','Label':'nowexternal-api','Depend':'api-service,nowmenu-api','Time':'09:00','Note':''},{'STT':12,'ID':'nowmenu-cron','Label':'nowmenu-cron','Depend':'','Time':'09:00','Note':''},{'STT':13,'ID':'nowapp-api','Label':'nowapp-api','Depend':'api-service,promotion-service','Time':'09:00','Note':''},{'STT':14,'ID':'nowapp-cron','Label':'nowapp-cron','Depend':'nowapp-api','Time':'09:00','Note':''},{'STT':15,'ID':'accountant-api','Label':'accountant-api','Depend':'','Time':'09:00','Note':''},{'STT':16,'ID':'accountant-cron','Label':'accountant-cron','Depend':'','Time':'09:00','Note':''},{'STT':17,'ID':'nownotify-api','Label':'nownotify-api','Depend':'','Time':'09:00','Note':''},{'STT':18,'ID':'nowaccount-api','Label':'nowaccount-api','Depend':'','Time':'09:00','Note':''},{'STT':19,'ID':'nowaccount-kafka-consumer','Label':'nowaccount-kafka-consumer','Depend':'','Time':'09:00','Note':''},{'STT':20,'ID':'nowauth-api','Label':'nowauth-api','Depend':'','Time':'09:00','Note':''},{'STT':21,'ID':'nowpay-api','Label':'nowpay-api','Depend':'','Time':'09:00','Note':''},{'STT':22,'ID':'nowpartner-api','Label':'nowpartner-api','Depend':'','Time':'10:00','Note':''},{'STT':23,'ID':'nowpartner-cron','Label':'nowpartner-cron','Depend':'','Time':'10:00','Note':''},{'STT':24,'ID':'gofast-api','Label':'gofast-api','Depend':'','Time':'10:00','Note':''},{'STT':25,'ID':'gofast-cron','Label':'gofast-cron','Depend':'','Time':'10:00','Note':''},{'STT':26,'ID':'promotion-service','Label':'promotion-service','Depend':'','Time':'09:00','Note':''}]
def test_topology(list_of_records=None):
    if not list_of_records:
        list_of_records = LIST_OF_RECORDS

    apps = topology.preprocessData(list_of_records)
    jobs_order = topology.topologicalSort(apps)
    print(jobs_order[1])

    list_nodes, list_edges = topology.prepareToDraw(apps)
    topology.drawGraph(list_nodes, list_edges)