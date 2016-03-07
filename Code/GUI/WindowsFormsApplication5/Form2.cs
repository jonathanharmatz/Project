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

namespace WindowsFormsApplication5
{
    public partial class Form2 : Form
    {
        public Form2()
        {
            InitializeComponent();
        }

        private void Form2_Load(object sender, EventArgs e)
        {

        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {

        }

        private void label2_Click(object sender, EventArgs e)
        {

        }

        private void textBox4_TextChanged(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
           
           var  server = new NamedPipeServerStream("NPtest1");
           Console.WriteLine("Waiting for connection...");
           server.WaitForConnection();
           Console.WriteLine("Connected.");
           var br = new BinaryReader(server);
           var bw = new BinaryWriter(server);
           string UN = username2.Text;
           string PW = password2.Text;
           string EM = email.Text;
           string FD = folderdir.Text;
           string[] send = new string[5];
           send[0]="register";
           send[1]=UN;
           send[2]=PW;
           send[3]=EM;
           send[4]=FD;
           for(int i=0; i<send.Length;i++)
                
                
                try
                {
                    
                     var str = new string(send[i].ToArray());  // Just for fun

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
           
                     var len2 = (int)br.ReadUInt32();            // Read string length
                     var str2 = new string(br.ReadChars(len2));    // Read string
                     MessageBox.Show(str2);  

            
            
        }
        }
    }

