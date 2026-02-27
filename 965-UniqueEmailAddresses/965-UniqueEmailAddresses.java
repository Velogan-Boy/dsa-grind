// Last updated: 2/27/2026, 5:11:20 PM
class Solution {
    public int numUniqueEmails(String[] emails) {

        int count = 0;

        if(emails.length == 0) {
            return count;
        }

        HashSet<String> hs = new HashSet<>();
                
        for(int i = 0; i < emails.length; i++){
            String[] split =  emails[i].split("@");

            String localName = split[0].split("\\+")[0].replace(".","");
            String domainName = split[1];

            hs.add(localName+"@"+domainName);
        }

        return hs.size();
        
    }
}