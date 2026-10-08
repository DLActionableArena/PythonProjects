from common.storage import JSONKeyValueStore

if __name__ == "__main__":
    store = JSONKeyValueStore("store", "task_data.json")
    store.set("agent_42_todo", "Verify customs paperwork")
    store.set("agent_99_status", "Credentials expired")
    print(store.get("agent_42_todo"))
    store.list_all()
    store.delete("agent_49_status") 
    store.list_all()    