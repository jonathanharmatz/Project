using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;
using System.IO.Pipes;

using System.Threading.Tasks;

namespace WindowsFormsApplication5
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            //var  server = new NamedPipeServerStream("NPtest");

           

            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
           var  server = new NamedPipeServerStream("NPtest1");
           Console.WriteLine("Waiting for connection...");
           server.WaitForConnection();
           Console.WriteLine("Connected.");
           var br = new BinaryReader(server);
           var bw = new BinaryWriter(server);
           string UN = username.Text;
           string PW = password.Text;
           string[] send = new string[3];
           send[0] = "login"; 
           send[1]=UN;
           send[2]=PW;
           for(int i=0; i<send.Length;i++)
                
                
                try
                {
                    var len = (int)br.ReadUInt32();            // Read string length
                    var str = new string(br.ReadChars(len));    // Read string

                    Console.WriteLine("Read: \"{0}\"", str);
                    
                    
                    str = new string(send[i].ToArray());  // Just for fun

                    var buf = Encoding.ASCII.GetBytes(str);     // Get ASCII byte array     
                    bw.Write((uint)buf.Length);                // Write string length
                    bw.Write(buf);                              // Write string
                    Console.WriteLine("Wrote: \"{0}\"", str);
                }
                catch (EndOfStreamException)
                {
                    Console.WriteLine("Client disconnected."); 
                    server.Close();
                    server.Dispose();   // When client disconnects
                }
            

            
            
        }

        private void Form1_Load(object sender, System.EventArgs e)
        {

        }

        private void username_TextChanged(object sender, EventArgs e)
        {

        }

        private void label1_Click(object sender, EventArgs e)
        {

        }

        private void label2_Click(object sender, EventArgs e)
        {

        }

        private void button2_Click(object sender, EventArgs e)
        {
            Form2 Register = new Form2();
            Register.Show();
            this.Hide();
 
        }

        
        }
    }

