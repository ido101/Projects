import javax.swing.*;
import java.awt.*;
public class Main {
    public static void main(String[] args) {

        JFrame frame = new JFrame();
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setVisible(true);
        frame.setTitle("Ido's Project");
        Image icon = Toolkit.getDefaultToolkit().getImage("C:\\Users\\IDO123\\Downloads\\pngwing.com-3.png");
        frame.setIconImage(icon);
        JLabel Title = new JLabel("Welcome! Please create an account");
        JLabel lbl = new JLabel("enter your name and password:");
        JTextField Tfield = new JTextField("Name");
        JPasswordField Pfield = new JPasswordField("Password");
        String[] Is13options = {"Im Below 13", "Im 13+"};
        JComboBox<String> Is13 = new JComboBox<>(Is13options);
        JButton btnA = new JButton("Create");
        Is13.setPreferredSize(new Dimension(frame.getWidth(), 50));
        Title.setPreferredSize(new Dimension(frame.getWidth(), 50));
        lbl.setPreferredSize(new Dimension(frame.getWidth(), 50));
        Tfield.setPreferredSize(new Dimension(frame.getWidth(), 50));
        Pfield.setPreferredSize(new Dimension(frame.getWidth(), 50));
        btnA.setPreferredSize(new Dimension(200, 50));
        frame.setLayout(new BoxLayout(frame.getContentPane(),BoxLayout.Y_AXIS));
        frame.add(Title);
        frame.add(lbl);
        frame.add(Tfield);
        frame.add(Pfield);
        frame.add(Is13);
        frame.add(btnA);
        btnA.setBounds(0, btnA.getY(), btnA.getWidth(), btnA.getHeight());
        frame.pack();
    }
}