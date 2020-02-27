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

        Session oldSession = null;

        public void Close()
        {
            if (oldSession != null)
                oldSession.Dispose();
        }

        public void ClientDidConnect(IWebSocketConnection webSocket)
        {
            string path = webSocket.ConnectionInfo.Path;
            Session session = null;
            if (oldSession != null)
            {
                session = oldSession;
                session.setWebSocket(webSocket);
            }
            else
                session = _sessionCreationDelegate(webSocket);
            oldSession = session;

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
                //if (oldSession1 != null && oldSession1 == session)
                //    oldSession1 = null;
                if (session != null)
                {
                    //webSocket.OnMessage = null;
                    //webSocket.OnBinary = null;
                    session.setWebSocket(null);
                    //session.Dispose();
                    //session = null;
                }
                //oldSession1 = null;
            };
        }
    }
}
