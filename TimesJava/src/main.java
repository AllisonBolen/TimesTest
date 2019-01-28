/** Show how you
 * would create a new subscriber and how you would add/remove a newsletter subscription for that subscriber.
 * Keep the solution simple. No need to interface with a database.
 * */

public class main {


    public static void main(String[] args){
        // new user
        TimesSubscriber userOne = new TimesSubscriber("Kevin", "Tao", "taok@mail.com");
        // new sub
        TimesSubscription subOne = new TimesSubscription("NYT Cooking", 1234567);
        // add subOne to userOne
        userOne.addSubscription(subOne);
        System.out.println(userOne);

        // add another subscription
        TimesSubscription subTwo = new TimesSubscription("Crossword", 7654321);
        userOne.addSubscription(subTwo);
        System.out.println(userOne);

        // remove subscription
        userOne.removeSubscription(subOne);
        System.out.println(userOne);

    }


}
