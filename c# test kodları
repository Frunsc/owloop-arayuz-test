using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Net;
using System.Net.Sockets;
using Newtonsoft.Json.Linq;
using System.IO;
using static System.Windows.Forms.VisualStyles.VisualStyleElement;






namespace Owloop_arayuz

{
    public partial class Form1 : Form
    {

        int port;
        string message;
        int byteCount;
        NetworkStream stream;
        byte[] sendData;
        TcpClient client;

        string saved;
        string yol = @"C:\Users\Sefa\Desktop\metin_belgesi.txt";

        public Form1()
        {
            InitializeComponent();
        }

        public void mesaj_gonder(string msg, string output)
        {
            if (client == null || !client.Connected)
            {
                Output.Items.Add("bağlantı bulunamadı");
            }
            else
            {
                NetworkStream stream = client.GetStream();
                if (stream.CanWrite && stream != null)
                {

                    string message = msg;
                    byte[] data = System.Text.Encoding.ASCII.GetBytes(message);
                    stream.Write(data, 0, data.Length);
                    Output.Items.Add(output);

                }

            }
        }

        private void toolStripButton8_Click(object sender, EventArgs e)
        {
            panel2.Visible = true;
            panel3.Visible = false;
            panel4.Visible = false;
            panel5.Visible = false;
            panel6.Visible = false;
            panel7.Visible = false;
            panel8.Visible = false;


        }

        private void toolStripButton2_Click(object sender, EventArgs e)
        {
            panel2.Visible = false;
            panel3.Visible = true;
            panel4.Visible = false;
            panel5.Visible = false;
            panel6.Visible = false;
            panel7.Visible = false;
            panel8.Visible = false;
        }

        private void toolStripButton5_Click(object sender, EventArgs e)
        {
            panel2.Visible = false;
            panel3.Visible = false;
            panel4.Visible = true;
            panel5.Visible = false;
            panel6.Visible = false;
            panel7.Visible = false;
            panel8.Visible = false;
        }


        private void toolStripButton3_Click(object sender, EventArgs e)
        {
            panel2.Visible = false;
            panel3.Visible = false;
            panel4.Visible = false;
            panel5.Visible = true;
            panel6.Visible = false;
            panel7.Visible = false;
            panel8.Visible = false;
        }

        private void toolStripButton4_Click(object sender, EventArgs e)
        {
            panel2.Visible = false;
            panel3.Visible = false;
            panel4.Visible = false;
            panel5.Visible = false;
            panel6.Visible = true;
            panel7.Visible = false;
            panel8.Visible = false;

        }

        private void toolStripButton6_Click(object sender, EventArgs e)
        {
            panel2.Visible = false;
            panel3.Visible = false;
            panel4.Visible = false;
            panel5.Visible = false;
            panel6.Visible = false;
            panel7.Visible = true;
            panel8.Visible = false;

        }

        private void toolStripButton7_Click(object sender, EventArgs e)
        {
            panel2.Visible = false;
            panel3.Visible = false;
            panel4.Visible = false;
            panel5.Visible = false;
            panel6.Visible = false;
            panel7.Visible = false;
            panel8.Visible = true;

        }


        private void button4_Click(object sender, EventArgs e)
        {

            if (!int.TryParse(textBox1.Text, out port))
            {

                MessageBox.Show("Port number not valied");
                Output.Items.Add("Port number invalied");
            }


            try
            {
                client = new TcpClient(textBox2.Text, port);

                MessageBox.Show("Connection Made");
                Output.Items.Add("Made connection with " + textBox2.Text);
                NetworkStream stream = client.GetStream();
                string message = "connected";
                byte[] data = System.Text.Encoding.ASCII.GetBytes(message);
                stream.Write(data, 0, data.Length);
            }
            catch (System.Net.Sockets.SocketException)
            {

                MessageBox.Show("Connection Failed");
                Output.Items.Add("Connection failed");
            }

        }

        private void button5_Click(object sender, EventArgs e)
        {
            try
            {
                message = textBox3.Text;
                byteCount = Encoding.ASCII.GetByteCount(message);
                sendData = new byte[byteCount];
                sendData = Encoding.ASCII.GetBytes(message);
                stream = client.GetStream();
                stream.Write(sendData, 0, sendData.Length);
                Output.Items.Add("Sent Data " + message);
            }
            catch (System.NullReferenceException)
            {

                MessageBox.Show("Connection not installised");
                Output.Items.Add("Failed to send data");
            }

        }

        private void button6_Click(object sender, EventArgs e)
        {
            mesaj_gonder("baglantiyi_kes", "BAGLANTI KESILDI");

        }



        private void button8_Click(object sender, EventArgs e)
        {
            mesaj_gonder("ledac", "LED ACILDI");


        }

        private void button7_Click(object sender, EventArgs e)
        {
            mesaj_gonder("ledkapat", "LED KAPATILDI");


        }

        private void button1_Click(object sender, EventArgs e)
        {
            mesaj_gonder("baslat", "MOTOR BASLATILDI");

        }

        private void button2_Click(object sender, EventArgs e)
        {
            mesaj_gonder("kapat", "ACIL FREN DEVREYE GIRDI");


        }

        private void button3_Click(object sender, EventArgs e)
        {
            mesaj_gonder("finish", "KAPSUL GERI CAGIRILIYOR");


        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            if (client == null || !client.Connected)
            {
                return;
            }

            try
            {
                NetworkStream stream = client.GetStream();

                if (stream.DataAvailable)
                {
                    byte[] data = new byte[2048];
                    int bytesRead = stream.Read(data, 0, data.Length);
                    string receivedData = Encoding.ASCII.GetString(data, 0, bytesRead);



                    var veriler = JObject.Parse(receivedData);


                    label3.Text = veriler["sicaklik"].ToString();
                    label31.Text = veriler["ivme"].ToString();
                    label27.Text = veriler["konum"].ToString();
                    label28.Text = veriler["konum"].ToString();
                    label29.Text = veriler["konum"].ToString();
                    label30.Text = veriler["konum"].ToString();
                    label25.Text = veriler["hiz"].ToString();
                    label26.Text = veriler["hiz"].ToString();
                    label33.Text = veriler["basinc"].ToString();
                    listBox1.Items.Add(veriler["konum"]);



                    using (StreamWriter writer = new StreamWriter(yol, true))
                    {
                        writer.WriteLine(receivedData);
                    }

                }
            }
            catch (Exception ex)
            {
                Console.WriteLine("HATA: " + ex.Message);
            }
        }

        private void button9_Click(object sender, EventArgs e)
        {
            NetworkStream stream = client.GetStream();
            string message = "kapat";
            byte[] data = System.Text.Encoding.ASCII.GetBytes(message);
            stream.Write(data, 0, data.Length);


        }



        private void button10_Click(object sender, EventArgs e)
        {
            if (client == null || !client.Connected)
            {
                Output.Items.Add("bağlantı bulunamadı");
            }
            else
            {
                NetworkStream stream = client.GetStream();
                string message = "thread";
                byte[] data = System.Text.Encoding.ASCII.GetBytes(message);
                stream.Write(data, 0, data.Length);
                Output.Items.Add("KAPSUL GERI CAGIRILIYOR");

            }


        }


    }
}
