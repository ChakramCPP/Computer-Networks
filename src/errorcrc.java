import java.io.*;
import java.util.ArrayList;

public class errorcrc
{
    public boolean check_parity(ArrayList<Integer>r,ArrayList<Integer>c)
    {
//        int cnts=0,cntr=0,parity;
//        for(int i=0;i<(r.size()-1);i++)
//        {
//            if(r.get(i) ==0)
//                continue;
//            else
//            {
//                cntr++;
//            }
//        }
//        parity=cntr%2;
//        if(r.get(r.size()-1)==parity) {
//            return true;
//        }
//        return false;
        int lp=0,rp=0;
         rp=lp+3;

        for(;rp<=(r.size()-1);lp++,rp++)
        {

            if(r.get(lp)==0)
            {
                for(;r.get(lp)==0;lp++);
            }
            rp=lp+3;
            for(int i=lp,j=0;i<=rp;i++,j++)
            {
                int ne=r.get(i)^c.get(j);
                r.set(i,ne);
            }

        }
        int s=r.size();
        if(r.get(s-1)==0)
        {
            if(r.get(s-2)==0)
            {
                if(r.get(s-3)==0)
                    return true;
            }

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
        ArrayList<Integer> crc= new ArrayList<>();

        for (int i=0;i<size;i++)
        {
            sd.add(Integer.parseInt(br.readLine()));
        }
        System.out.println("Enter the receiver Data:");
        for (int i=0;i<size;i++)
        {

            rd.add(Integer.parseInt(br.readLine()));
        }
        System.out.println("Enter the CRC size and data:");
        int crcsize=Integer.parseInt(br.readLine());
        for(int i=0;i<crcsize;i++)
        {
            crc.add(Integer.parseInt(br.readLine()));
        }
        errorcrc er= new errorcrc();
        if(er.check_parity(rd,crc))
        {
            System.out.println("Data Transfer Successful");
        }
        else
        {
            System.out.println("Error!!");
        }

    }

}

