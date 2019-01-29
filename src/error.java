import java.io.*;
import java.util.ArrayList;

public class error
{
    public boolean check_parity(ArrayList<Integer>r)
    {
        int cnts=0,cntr=0,parity;
        for(int i=0;i<(r.size()-1);i++)
        {
            if(r.get(i) ==0)
                continue;
            else
            {
                cntr++;
            }
        }
      parity=cntr%2;
        if(r.get(r.size()-1)==parity) {
            return true;
        }
        return false;
     }

    public static void main(String args[]) throws IOException
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        System.out.println("Enter the sender Data size:");
        int size= Integer.parseInt(br.readLine());
        ArrayList<Integer> sd= new ArrayList<>();
        ArrayList<Integer> rd= new ArrayList<>();
        for (int i=0;i<size;i++)
        {
            sd.add(Integer.parseInt(br.readLine()));
        }
        System.out.println("Enter the receiver Data:");
        for (int i=0;i<size;i++)
        {

            rd.add(Integer.parseInt(br.readLine()));
        }

        error er= new error();
        if(er.check_parity(rd))
        {
            System.out.println("Data Transfer Successful");
        }
        else
        {
            System.out.println("Error!!");
        }

    }

}
