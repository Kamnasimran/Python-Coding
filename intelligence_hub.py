# setdefault() is useful for the Movement Log because it creates an empty
# list for an agent automatically on its first move and returns the existing
# list on later moves. This avoids separate initialization code. A tuple is
# suitable for Location because coordinates should remain fixed as one
# coordinate pair. Tuples are immutable, so a location cannot be changed
# item by item. A new tuple must be created when an agent is relocated.

agent_registry = {
    "Agent_Alpha": {
        "Location": (10, 20),
        "Knowledge": {
            "grid map",
            "comm protocol",
            "telemetry sync"
        }
    },
    "Agent_Beta": {
        "Location": (15, 5),
        "Knowledge": {
            "grid map",
            "comm protocol",
            "power grid"
        }
    },
    "Agent_Gamma": {
        "Location": (0, 0),
        "Knowledge": {
            "grid map",
            "comm protocol",
            "power grid",
            "telemetry sync"
        }
    }
}


def find_common_intelligence(registry):
    knowledge_sets = [
        agent_data["Knowledge"]
        for agent_data in registry.values()
    ]

    return set.intersection(*knowledge_sets)


def relocate_agent(registry, log, agent_id, new_location):

    try:
        registry[agent_id]["Location"][0] = new_location[0]

    except TypeError:
        print(
            "TypeError caught: tuple object does not support item assignment"
        )
        print(
            "Tuples are immutable; reassigning a new tuple instead."
        )

    registry[agent_id]["Location"] = new_location

    log.setdefault(agent_id, []).append(new_location)


print("--- Common Intelligence Across All Agents ---")

common_intelligence = find_common_intelligence(
    agent_registry
)

print(common_intelligence)


movement_log = {}

print()
print("--- Relocating Agent_Alpha ---")

print(
    "Attempting direct mutation of Agent_Alpha's Location tuple..."
)

relocate_agent(
    agent_registry,
    movement_log,
    "Agent_Alpha",
    (12, 22)
)

print(
    "Agent Alpha new state:",
    agent_registry["Agent_Alpha"]
)

print("Movement Log:", movement_log)


print()
print("--- Relocating Agent Alpha again ---")

relocate_agent(
    agent_registry,
    movement_log,
    "Agent_Alpha",
    (14, 25)
)

print("Movement Log:", movement_log)


summary_report = {
    agent_id: len(data["Knowledge"])
    for agent_id, data in agent_registry.items()
}

print()
print(
    "--- Summary Report (Dictionary Comprehension) ---"
)

print(summary_report)


print()
print("--- Edge Case 1: Empty Knowledge Set ---")

edge_registry = {
    "Agent_Empty": {
        "Location": (5, 5),
        "Knowledge": set()
    },
    "Agent_Test": {
        "Location": (1, 1),
        "Knowledge": {
            "grid map",
            "comm protocol"
        }
    }
}

edge_common = find_common_intelligence(edge_registry)

print("Common intelligence:", edge_common)

assert edge_common == set()

print("Edge Case 1 passed")


print()
print("--- Edge Case 2: First Relocation ---")

first_move_log = {}

relocate_agent(
    agent_registry,
    first_move_log,
    "Agent_Beta",
    (20, 30)
)

print("Movement Log:", first_move_log)

assert first_move_log == {
    "Agent_Beta": [(20, 30)]
}

print("Edge Case 2 passed")


print()
print("--- Edge Case 3: Zero Knowledge Summary ---")

zero_knowledge_registry = {
    "Agent_Zero": {
        "Location": (0, 0),
        "Knowledge": set()
    },
    "Agent_Known": {
        "Location": (1, 1),
        "Knowledge": {
            "grid map"
        }
    }
}

zero_summary = {
    agent_id: len(data["Knowledge"])
    for agent_id, data in zero_knowledge_registry.items()
}

print("Summary Report:", zero_summary)

assert zero_summary["Agent_Zero"] == 0

print("Edge Case 3 passed")

print()
print("All tests passed")
