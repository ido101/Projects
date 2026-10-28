import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int num1,num2;
        int count = 0;
        int sum = 0;
        int equal=0;
        num1 = in.nextInt();
        num2 = in.nextInt();
        while (num1 + num2 != 0){
            count+=2;
            if(num1==num2){
                equal++;
            }
            if(num1 > 0){
                sum += num1;
            }
            if(num2 > 0){
                sum += num2;
            }
            num1 = in.nextInt();
            num2 = in.nextInt();
        }
        count+=2;
        if(num1 > 0){
            sum += num1;
        }
        if(num2 > 0){
            sum += num2;
        }
        System.out.println("Count: " + count);
        System.out.println("Equals: " + equal);
        System.out.println("Sum: " + sum);
    }
    public static void printByYear(Child[] arr, int year ){
        int CountM = 0;
        int CountF = 0;
        for(int i = 0; i < arr.length; i++){
            if(arr[i].getYear() == year){
                if(arr[i].getGender() == 'M'){
                    CountM++;
                }else{
                    CountF++;
                }
            }
        }
    }
    public static void printByMonth(Child[] arr){
        int[] array = {0,0,0,0,0,0,0,0,0,0,0,0};
        for(int i = 0; i < arr.length; i++){
            array[arr[i].getMonth()-1   ]++;
        }
    }
    public static void M(int num){
        int arr[] = new int[num];
        
    }
}