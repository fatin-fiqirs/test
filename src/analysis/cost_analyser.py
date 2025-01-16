class CostAnalyzer:
    def __init__(self):
        self.routes = []
        self.costs = {}
    
    def add_route(self, route_data):
        """Add route data for analysis"""
        self.routes.append(route_data)
    
    def calculate_costs(self):
        """Calculate route costs"""
        total_distance = 0
        total_fuel = 0
        total_time = 0
        
        for route in self.routes:
            total_distance += route['distance']
            total_fuel += route['fuel_consumed']
            total_time += route['time']
        
        self.costs = {
            'cost_per_mile': total_fuel * 3.5 / total_distance,
            'time_efficiency': total_distance / total_time,
            'fuel_efficiency': total_distance / total_fuel
        }
        
        return self.costs
