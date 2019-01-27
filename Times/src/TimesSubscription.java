/** Represent a newsletter subscription as a separate entity that includes a name and a code or ID.  */
public class TimesSubscription {

    private String name;
    private int subId;

    //** Basic constructor, no defaults */
    public TimesSubscription() {

    }

    //** Overloaded constructor for setting up defaults. */
    public TimesSubscription(String subName, int sId) {
        this.name = subName;
        this.subId = sId;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getSubId() {
        return subId;
    }

    public void setSubId(int subId) {
        this.subId = subId;
    }

    public String toString(){
        return "\n\t\t"+ this.name + ": "+ this.subId;
    }
}
