import java.util.ArrayList;

/** Write a representation of a New York Times newsletter subscriber.
 * Make sure the subscriber has a first name, last name, email address, and a list of newsletter subscriptions.
 * Represent a newsletter subscription as a separate entity that includes a name and a code or ID. Show how you
 * would create a new subscriber and how you would add/remove a newsletter subscription for that subscriber.
 * Keep the solution simple. No need to interface with a database.*/


import java.util.HashMap;
import java.util.Map;

public class TimesSubscriber {

    private String firstName, lastName, emailAddress;
    private HashMap<Integer,TimesSubscription> subscritptionList; // hashmap ensuring unique list of subscription ids that the user follows.

    //** Overloaded constructor for setting up defaults. */
    public TimesSubscriber(String fName, String lName, String email) {
        this.emailAddress = email;
        this.firstName = fName;
        this.lastName = lName;

        subscritptionList = new HashMap<Integer,TimesSubscription>();
    }

    //** Basic constructor, no defaults */
    public TimesSubscriber() {

    }

    /// setters and getters

    public String getFirstName() {
        return firstName;
    }

    public void setFirstName(String firstName) {
        this.firstName = firstName;
    }

    public String getLastName() {
        return lastName;
    }

    public void setLastName(String lastName) {
        this.lastName = lastName;
    }

    public String getEmailAddress() {
        return emailAddress;
    }

    public void setEmailAddress(String emailAddress) {
        this.emailAddress = emailAddress;
    }

    public HashMap<Integer,TimesSubscription> getSubscritptionList() {
        return subscritptionList;
    }

    public void setSubscritptionList(HashMap<Integer,TimesSubscription> subscritptionList) {
        this.subscritptionList = subscritptionList;
    }

    //// subscription list modifiers

    public void addSubscription(TimesSubscription newSubscription){
        subscritptionList.put(newSubscription.getSubId(), newSubscription);
    }

    public void removeSubscription(TimesSubscription deleteSubscription){
        subscritptionList.remove(deleteSubscription.getSubId());
    }

    public String toString(){
        String info =  "\tName: "+ this.lastName + ", " +this.firstName + "\n\tEmail: "+ this.emailAddress + "\n\tSubscriptions: ";
        for (Map.Entry<Integer, TimesSubscription> entry : subscritptionList.entrySet()){
            info += entry.getValue().toString();
        }
        return info;
    }

}
