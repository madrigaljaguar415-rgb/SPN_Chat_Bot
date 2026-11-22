self.addEventListener('install', (e) => {
  self.skipWaiting();
});
self.addEventListener('fetch', (e) => {
  e.respondWith(fetch(e.request).catch(() => {
    return new Response('You are offline. Please connect to internet to use SPN.');
  }));
});