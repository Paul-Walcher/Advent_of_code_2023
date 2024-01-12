
using System;
using System.IO;
using System.Collections.Generic;

namespace Program{

    class Program{

        protected static Int64 hash(string code){
            
            Int64 val = 0;

            foreach(char c in code){
                val += (Int64)c;
                val *= 17;
                val %= 256;
            }

            return val;
        }

        public static void Main(string[] args){

            string path = args[0];
            StreamReader sr = new StreamReader(path);
            string line;

            line = sr.ReadLine();
            sr.Close();
            string[] data = line.Split(',');

            Int64 summe = 0;
            foreach(string dp in data){
                summe += Program.hash(dp);
            }
            Console.WriteLine(summe);




        }

    }

}