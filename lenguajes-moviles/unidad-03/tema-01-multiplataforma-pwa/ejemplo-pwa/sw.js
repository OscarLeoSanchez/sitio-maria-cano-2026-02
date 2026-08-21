// Service worker mínimo: cache-first para que la página cargue sin conexión.
const CACHE_NOMBRE = "guia-bolsillo-v1";
const ARCHIVOS_A_CACHEAR = [
  "./",
  "./index.html",
  "./manifest.json",
  "./icon.svg"
];

self.addEventListener("install", (event) => {
  event.waitUntil(
    caches.open(CACHE_NOMBRE).then((cache) => cache.addAll(ARCHIVOS_A_CACHEAR))
  );
});

self.addEventListener("activate", (event) => {
  event.waitUntil(
    caches.keys().then((nombres) => {
      return Promise.all(
        nombres
          .filter((nombre) => nombre !== CACHE_NOMBRE)
          .map((nombre) => caches.delete(nombre))
      );
    })
  );
});

self.addEventListener("fetch", (event) => {
  event.respondWith(
    caches.match(event.request).then((respuestaCacheada) => {
      return respuestaCacheada || fetch(event.request);
    })
  );
});
