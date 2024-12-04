import psutil  # To check battery status
import time    # To add delays
from win10toast import ToastNotifier  # For notifications


def notify_battery_status():
    """
    This function checks the battery percentage and charging status.
    It notifies the user when:
    - Battery is above 80% and charger is still plugged in
    - Battery is below 25% and charger is unplugged
    """    
    toaster = ToastNotifier();  # Initialize the notifier for toast messages
    battery = psutil.sensors_battery(); # Get battery information

    if battery:
        # Get battery percentage and charging status
        percentage = battery.percent;
        is_charging = battery.power_plugged;

        # Notify user if battery is above 80% and still charging
        if percentage >= 80 and is_charging:
            toaster.show_toast(
                "Battery Alert",
                f"Battery is at {percentage}%. Please unplug the charger.",
                duration = 10,
                icon_path = None
            );            
        # Notify user if battery is below 25% and not charging
        elif percentage <= 25 and not is_charging:
            toaster.show_toast(
                "Battery Alert",
                f"Battery is at {percentage}%. Please plug the charger.",
                duration = 10,
                icon_path = None
            );
        # Notify the current battery percentage and charging status(for checking purpose)
        # else:
        #     toaster.show_toast(
        #         "Battery Alert",
        #         f"Battery is at {percentage}%. Charging: {'Yes' if is_charging else 'No'}.",
        #         duration = 10,
        #         icon_path = None
        #     );

if __name__ == "__main__":
    """
    Main function to repeatedly check battery status every minute.
    """
    while True:
        notify_battery_status();     # Check and notify battery status
        time.sleep(60);              # Wait for 1 minute before checking again
