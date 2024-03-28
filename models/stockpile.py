class Stockpile:
    def __init__(self):
        self.resources = {}
        self.capacity = {}  # Stores the maximum capacity for resources

    # Set the maximum capacity for each resource in stockpile.
    def set_stockpile_capacity(self, capacities):
        self.capacity = capacities

    # Adds a specified amount of a resource to the stockpile, respecting the capacity limit.
    def add_to_stockpile(self, label, value):
        if label in self.capacity:
            # Ensure not to exceed the set capacity
            if label in self.resources:
                potential_total = self.resources[label] + value
                # If adding the value exceeds capacity, set to max capacity, else add normally
                self.resources[label] = min(potential_total, self.capacity[label])
            else:
                # If resource not present, add it respecting the capacity
                self.resources[label] = min(value, self.capacity[label])
        else:
            # If no capacity limit is set, just add the resource
            if label in self.resources:
                self.resources[label] += value
            else:
                self.resources[label] = value

    # Stock a specified amount for each resource, respecting the maximum capacities.
    def stock_resources(self, resources):
        for label, value in resources.items():
            self.add_to_stockpile(label, value)

    def consume_from_stockpile(self, label, value):
        if label in self.resources and self.resources[label] >= value:
            self.resources[label] -= value
        elif label not in self.resources:
            print(f"The resource {label} is not available in the stockpile.")
        else:
            print(f"Not enough of the resource {label} available to consume.")

    def print_stockpile_info(self, entity_label):
        print(f"Stockpile for {entity_label}:")
        if not self.resources:
            print("  No resources in the stockpile.")
            return
        longest_label_length = max(len(label) for label in self.resources.keys())
        for label, value in sorted(self.resources.items()):
            formatted_value = f"{int(value)}" if value >= 0 else f"{value}"
            print(f"  {label.rjust(longest_label_length)}: {formatted_value} units")