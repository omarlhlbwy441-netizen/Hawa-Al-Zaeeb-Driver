# Wolf Driver (design framework)
نظام إدارة الطلبات المتكامل القائم على الذكاء الاصطناعي.

## التشغيل السريع
1. تأكد من تثبيت Docker.
2. شغل الأمر التالي:
   docker-compose up --build

## الهيكلية
- /services/api_gateway: FastAPI backend.
- /services/ai_engine: LangChain smart agent.
- /clients/web_dashboard: React + Redux dashboard.