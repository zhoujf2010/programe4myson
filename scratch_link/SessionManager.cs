using Fleck;
using System;
using System.Windows;

namespace scratch_link
{
    internal class SessionManager
    {
        public int ActiveSessionCount { get; private set; }

        private readonly Func<IWebSocketConnection, Session> _sessionCreationDelegate;

        internal SessionManager(Func<IWebSocketConnection, Session> sessionCreationDelegate)
        {
            ActiveSessionCount = 0;
            _sessionCreationDelegate = sessionCreationDelegate;
        }

        static Session oldSession1 = null;
        static Session oldSession2 = null;
        static Session oldSession3 = null;

        public void Close()
        {
            if (oldSession1 != null)
                oldSession1.Dispose();
            if (oldSession2 != null)
                oldSession2.Dispose();
            if (oldSession3 != null)
                oldSession3.Dispose();
        }

        public void ClientDidConnect(IWebSocketConnection webSocket)
        {
            string path = webSocket.ConnectionInfo.Path;
            Session session = null;
            if (path.Contains("ble"))
            {
                if (oldSession1 != null)
                {
                    session = oldSession1;
                    session.setWebSocket(webSocket);
                }
                else
                    session = _sessionCreationDelegate(webSocket);
                oldSession1 = session;
            }
            else if (path.Contains("bt"))
            {
                if (oldSession2 != null)
                {
                    session = oldSession2;
                    session.setWebSocket(webSocket);
                }
                else
                    session = _sessionCreationDelegate(webSocket);
                oldSession2 = session;
            }
            else if (path.Contains("hc"))
            {
                if (oldSession3 != null)
                {
                    session = oldSession3;
                    session.setWebSocket(webSocket);
                }
                else
                    session = _sessionCreationDelegate(webSocket);
                oldSession3 = session;
            }

            //if (session is BTSession)
            //{
            //    if (oldSession1 != null)
            //    {
            //        --ActiveSessionCount;
            //        ((App)(Application.Current)).UpdateIconText();
            //        oldSession1.Dispose();
            //    }
            //    oldSession1 = session;
            //}

            webSocket.OnOpen = () =>
            {
                ++ActiveSessionCount;
                ((App)(Application.Current)).UpdateIconText();
            };
            webSocket.OnMessage = async message => await session.OnMessage(message);
            webSocket.OnBinary = async message => await session.OnBinary(message);
            webSocket.OnClose = () =>
            {
                --ActiveSessionCount;
                ((App)(Application.Current)).UpdateIconText();
                if (oldSession1 != null && oldSession1 == session)
                    oldSession1 = null;
                if (oldSession2 != null && oldSession2 == session)
                    oldSession2 = null;
                if (oldSession3 != null && oldSession3 == session)
                    oldSession3 = null;
                if (session != null)
                {
                    session.setWebSocket(null);
                    session.Dispose();
                    session = null;
                }
                //oldSession1 = null;
            };
        }
    }
}
