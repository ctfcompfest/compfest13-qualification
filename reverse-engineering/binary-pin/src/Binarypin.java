import java.awt.event.ActionListener;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;

import java.awt.event.ActionEvent;

class Secret {
    private int cnt;
    private int[] box;
    private int[] mydata;
    private static Secret instance = new Secret();

    private Secret() {
        this.cnt = 1;
        this.mydata = new int[]{0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0};
        int tmp = this.mydata.length / 9;
        this.box = new int[tmp];
    }

    public static Secret getInstance() {
        return instance;
    }

    public void resetInstance() {
        instance = new Secret();
    }

    public void process(char s) {
        if (this.cnt > 9) return;

        int k = this.mydata.length / 9;
        for(int i = 1; i <= k; i++) {
            int ri = 9 * i - this.cnt;
            int accum = this.box[i - 1] + this.mydata[ri];
            accum += s - '0';
            this.mydata[ri] = accum % 2;

            if (accum >= 2) this.box[i - 1] = 1;
            else this.box[i - 1] = 0;
        }
        this.cnt++;
    }

    private String misteri(int accum) {
        String f = "";
        int hrf = 0;
        for (int j = 1; accum > 0; j++) {
            hrf |= (accum & 1) << (j % 8 - 1);
            accum >>= 1;
            if (j % 8 == 0) {
                if (' ' <= hrf && hrf < 128)
                    f = (char) hrf + f;
                hrf = 0;
            }
        }
        f = (char) hrf + f;
        return f;
    }

    public String getData() {
        int k = this.mydata.length / 9;
        String ret = "";
        
        int sisa = 5;
        int accum = 0;
        for (int i = 1; i <= k; i++) {
            int tmp = 0;
            int n = 1;
            for (int j = 1; j <= 8; j++) {
                tmp += this.mydata[9 * i - j] * n;
                n <<= 1; 
            }
            sisa--;
            accum += (tmp - 33) * Math.pow(85, sisa);
            if (sisa == 0) {
                ret = ret + misteri(accum);
                accum = 0;
                sisa = 5;
            }
        }
        while(sisa > 0) {
            accum += 84 * Math.pow(85, --sisa);
        }
        return ret + misteri(accum);
    }
}

class PinButton extends JButton implements ActionListener {
    Binarypin app;

    PinButton(Binarypin app, String val, int x, int y, int width, int height) {
        super(val);
        this.app = app;
        this.addActionListener(this);
        this.setBounds(x, y, width, height);
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        Secret.getInstance().process(this.getText().charAt(0));
        this.app.updateOutput();
    }
}

class ResetButton extends JButton implements ActionListener {
    private Binarypin app;

    ResetButton(Binarypin app, int x, int y, int width, int height) {
        super("Reset");
        this.app = app;
        this.addActionListener(this);
        this.setBounds(x, y, width, height);
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        Secret.getInstance().resetInstance();
        this.app.clearOutput();
    }
}

public class Binarypin {
    private JFrame frame;
    private JLabel output;

    Binarypin () {
        frame = new JFrame("Binary Pin");

        output = new JLabel();
        output.setBounds(20, 250, 360, 20);
        
        JLabel tmpLabel = new JLabel("Your data:");
        tmpLabel.setBounds(20, 235, 100, 20);        

        frame.add(tmpLabel);
        frame.add(output);
        frame.add(new PinButton(this, "0", 43, 10, 150, 150));
        frame.add(new PinButton(this, "1", 198, 10, 150, 150));
        frame.add(new ResetButton(this, 43, 165, 305, 50));

        frame.setSize(400,350);  
        frame.setLayout(null);  
        frame.setVisible(true);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    }
    public static void main(String[] args) {
        new Binarypin();
    }

    public void clearOutput() {
        this.output.setText("");
    }

    public void updateOutput() {
        this.output.setText(Secret.getInstance().getData());
    }
}
