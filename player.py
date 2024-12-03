# Define the main Player class
class Player:
    def __init__(self, name, position, jersey_number, nationality):
        """
        Initialize the Player object with attributes.
        :param name: Name of the player
        :param position: Position on the field
        :param jersey_number: Jersey number of the player
        :param nationality: Nationality of the player (private)
        """
        self.name = name
        self.position = position
        self.jersey_number = jersey_number
        self.__nationality = nationality  # Private attribute (encapsulation)
    
    def display_info(self):
        """Display basic information about the player."""
        return (f"Player Name: {self.name}, Position: {self.position}, "
                f"Jersey Number: {self.jersey_number}")
    
    def get_nationality(self):
        """Access private nationality."""
        return self.__nationality
    
    def set_nationality(self, nationality):
        """Set private nationality with validation."""
        if isinstance(nationality, str) and nationality.strip():
            self.__nationality = nationality
        else:
            raise ValueError("Invalid nationality.")

# Define the Goalkeeper class, inheriting from Player
class Goalkeeper(Player):
    def __init__(self, name, jersey_number, nationality, clean_sheets=0):
        """
        Initialize the Goalkeeper object with attributes.
        :param clean_sheets: Number of clean sheets (default: 0)
        """
        super().__init__(name, "Goalkeeper", jersey_number, nationality)
        self.clean_sheets = clean_sheets
    
    def add_clean_sheet(self):
        """Increment the clean sheets count."""
        self.clean_sheets += 1
    
    def display_info(self):
        """Override to include clean sheet information."""
        return (super().display_info() + 
                f", Clean Sheets: {self.clean_sheets}")

# Define the Striker class, inheriting from Player
class Striker(Player):
    def __init__(self, name, jersey_number, nationality, goals=0):
        """
        Initialize the Striker object with attributes.
        :param goals: Number of goals scored (default: 0)
        """
        super().__init__(name, "Striker", jersey_number, nationality)
        self.goals = goals
    
    def score_goal(self):
        """Increment the goals count."""
        self.goals += 1
    
    def display_info(self):
        """Override to include goals information."""
        return (super().display_info() +
                f", Goals: {self.goals}")

# Demonstration of the classes
if __name__ == "__main__":
    # Creating a generic player
    player1 = Player("Luka Modric", "Midfielder", 10, "Croatia")
    print(player1.display_info())
    print("Nationality:", player1.get_nationality())

    # Creating a Goalkeeper and displaying details
    goalkeeper = Goalkeeper("Thibaut Courtois", 1, "Belgium", clean_sheets=5)
    print(goalkeeper.display_info())
    goalkeeper.add_clean_sheet()
    print("After another clean sheet:", goalkeeper.display_info())

    # Creating a Striker and displaying details
    striker = Striker("Cristiano Ronaldo", 7, "Portugal", goals=50)
    print(striker.display_info())
    striker.score_goal()
    print("After scoring a goal:", striker.display_info())

