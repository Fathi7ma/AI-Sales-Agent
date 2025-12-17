conversation_store = {}

def save_message(lead_id, role, message):
    conversation_store.setdefault(lead_id, [])
    conversation_store[lead_id].append({"role": role, "content": message})
    return conversation_store[lead_id][-5:]