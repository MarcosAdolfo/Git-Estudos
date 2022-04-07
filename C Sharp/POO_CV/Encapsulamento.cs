using System;

namespace POO
{

    abstract class Controlador
    {
        abstract public void ligar();
        abstract public void desligar();
        abstract public void abrirMenu();
        abstract public void fecharMenu();
        abstract public void maisVolume();
        abstract public void menosVolume();
        abstract public void ligarMudo();
        abstract public void desligarMudo();
        abstract public void play();
        abstract public void pause();
    }

    class ControleRemoto:Controlador
    {
        //----Atributos----
        private int volume;
        private bool ligado;
        private bool tocando;
        //----Métodos Especiais----
        public ControleRemoto()
        {
            volume = 50;
            ligado = false;
            tocando = false;
        }

         // volume
        public void setVolume(int volume)
        {
            this.volume = volume;
        }
        public int getVolume()
        {
            return this.volume;
        }
         // ligado
        public void setLigado(bool ligado)
        {
            this.ligado = ligado;
        }
        public bool getLigado()
        {
            return ligado;
        }
         // tocando
        public void setTocando(bool tocando)
        {
            this.tocando = tocando;
        }
        public bool getTocando()
        {
            return this.tocando;
        }

        //----Metodos Abistratos----
        override public void ligar()
        {
            setLigado(true);
        }
        override public void desligar()
        {
            setLigado(false);
        }
        override public void abrirMenu()
        {
            Console.WriteLine("----------Menu----------");
            Console.WriteLine("Ligado:.. {0}", this.getLigado());
            Console.WriteLine("Tocando:. {0}", getTocando());
            Console.Write("Volume:... {0}% :", this.getVolume());
            for(int i=1; i<=getVolume();i+=5)
            {
                Console.Write("|");
            }
            Console.WriteLine("\n-----------------------");
        }
        override public void fecharMenu()
        {
            Console.WriteLine("Fechando Menu...");
        }
        override public void maisVolume()
        {
            if(getLigado())
            {
                setVolume(getVolume()+5);
            }
        }
        override public void menosVolume()
        {
            if(getLigado())
            {
                setVolume(getVolume()-5);
            }
        }
        override public void ligarMudo()
        {
            if(getLigado() && getVolume()>0)
            {
                setVolume(0);
            }
        }
        override public void desligarMudo()
        {
            if(getLigado() && getVolume()<=0)
            {
                setVolume(50);
            }
        }
        override public void play()
        {
            if(getLigado() && !getTocando())
            {
                setTocando(true);
            }
        }
        override public void pause()
        {
            if(getLigado() && getTocando())
            {
                setTocando(false);
            }
        }
    }

    class Encapsulamento
    {
        static void Main(string[] args)
        {
            ControleRemoto c = new ControleRemoto();
            c.ligar();
            c.maisVolume();
            c.ligarMudo();
            c.desligarMudo();
            c.play();
            c.abrirMenu();
            c.fecharMenu();
        }
    }

}
