using System;

namespace Aula32
{

    class Cauculos
    {
        public int v1;
        public int v2;

        public Cauculos(int v1,int v2)
        {
            this.v1 = v1;
            this.v2 = v2;
        }

        public int Soma()
        {
            return v1+v2;
        }
    }

    class aula32
    {
        static void Main()
        {
            Cauculos c = new Cauculos(10,2);
            Console.WriteLine(c.Soma());
        }
    }

}