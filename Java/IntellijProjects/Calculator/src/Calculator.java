import javax.swing.*;

import java.awt.*;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
public class Calculator extends JFrame implements ActionListener
{

    private String str1, str2, str3;
    private static JTextField result;

    public Calculator(){
        str1 = str2 = str3 = "";
        result = new JTextField(16);
        result.setEditable(false);
    }

    public void actionPerformed(ActionEvent e)
    {
        String s = e.getActionCommand();
        if((s.charAt(0) >= '0'&& s.charAt(0) <= '9') || (s.charAt(0) == '.'))
        {
            if(!str2.equals("")) {str3 += s; }
            else { str1 += s; }
            result.setText(str1 + str2 + str3);
        }
        else if(s.charAt(0) == 'C'){
            str1 = str2 = str3 = "";
            result.setText("");
        }
        else if(s.charAt(0) == '='){
            double temp;
            if(str2.equals("+")) { temp = (Double.parseDouble(str1)) + (Double.parseDouble(str3)); }
            else if(str2.equals("-")) { temp = (Double.parseDouble(str1)) - (Double.parseDouble(str3));}
            else if(str2.equals("/")) {
                if(Double.parseDouble(str3) == 0){
                    result.setText("Error! division by zero.");
                    return;
                }
                temp = (Double.parseDouble(str1)) / (Double.parseDouble(str3)); }
            else { temp = (Double.parseDouble(str1)) * (Double.parseDouble(str3)); }
            result.setText(str1 + str2 + str3 + "=" + temp);
            str1 = Double.toString(temp);
            str2 = str3 = "";
        }
        else{
            if(str2.equals("")) {
                str2 += s;
            }
            result.setText(str1 + str2 + str3);
        }
    }

    public static void main(String[] args) {
        Calculator calc = new Calculator();
        JFrame frame = new JFrame("Calculator");

        JButton b0 = new JButton("0");
        JButton b1 = new JButton("1");
        JButton b2 = new JButton("2");
        JButton b3 = new JButton("3");
        JButton b4 = new JButton("4");
        JButton b5 = new JButton("5");
        JButton b6 = new JButton("6");
        JButton b7 = new JButton("7");
        JButton b8 = new JButton("8");
        JButton b9 = new JButton("9");
        JButton bAdd = new JButton("+");
        JButton bSub = new JButton("-");
        JButton bMul = new JButton("*");
        JButton bDiv = new JButton("/");
        JButton bEqual = new JButton("=");
        JButton bClear = new JButton("C");
        JButton bDot = new JButton(".");

        JPanel upperPanel = new JPanel();
        JPanel panel = new JPanel(new GridLayout(5, 4));
        upperPanel.setBackground(Color.BLUE);
        panel.setBackground(Color.BLUE);

        upperPanel.add(result);
        panel.add(b0);
        panel.add(b1);
        panel.add(b2);
        panel.add(b3);
        panel.add(b4);
        panel.add(b5);
        panel.add(b6);
        panel.add(b7);
        panel.add(b8);
        panel.add(b9);
        panel.add(bAdd);
        panel.add(bSub);
        panel.add(bMul);
        panel.add(bDiv);
        panel.add(bEqual);
        panel.add(bClear);
        panel.add(bDot);

        b0.addActionListener(calc);
        b1.addActionListener(calc);
        b2.addActionListener(calc);
        b3.addActionListener(calc);
        b4.addActionListener(calc);
        b5.addActionListener(calc);
        b6.addActionListener(calc);
        b7.addActionListener(calc);
        b8.addActionListener(calc);
        b9.addActionListener(calc);
        bAdd.addActionListener(calc);
        bSub.addActionListener(calc);
        bMul.addActionListener(calc);
        bDiv.addActionListener(calc);
        bEqual.addActionListener(calc);
        bClear.addActionListener(calc);
        bDot.addActionListener(calc);

        frame.setLayout(new BorderLayout());
        frame.add(upperPanel, BorderLayout.NORTH);
        frame.add(panel, BorderLayout.EAST);
        frame.add(panel, BorderLayout.WEST);
        frame.add(panel, BorderLayout.SOUTH);
        frame.add(panel, BorderLayout.CENTER);

        frame.setSize(210, 220);
        frame.setLocationRelativeTo(null);
        frame.setVisible(true);
        frame.setDefaultCloseOperation(EXIT_ON_CLOSE );
    }

}