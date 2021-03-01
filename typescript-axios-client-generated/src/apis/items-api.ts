/* tslint:disable */
/* eslint-disable */
/**
 * FastAPI Vue RabbitMQ PostgreSQL Traefik full set of applications for organizing auto-dialing on Asterisk
 * No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)
 *
 * OpenAPI spec version: 0.1.0
 * 
 *
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 * Do not edit the class manually.
 */
import globalAxios, { AxiosPromise, AxiosInstance } from 'axios';
import { Configuration } from '../configuration';
// Some imports not used depending on template conditions
// @ts-ignore
import { BASE_PATH, COLLECTION_FORMATS, RequestArgs, BaseAPI, RequiredError } from '../base';
import { HTTPValidationError } from '../models';
import { Item } from '../models';
import { ItemCreate } from '../models';
import { ItemUpdate } from '../models';
/**
 * ItemsApi - axios parameter creator
 * @export
 */
export const ItemsApiAxiosParamCreator = function (configuration?: Configuration) {
    return {
        /**
         * Create new item.
         * @summary Create Item
         * @param {ItemCreate} body 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        createItemApiV1ItemsPost: async (body: ItemCreate, options: any = {}): Promise<RequestArgs> => {
            // verify required parameter 'body' is not null or undefined
            if (body === null || body === undefined) {
                throw new RequiredError('body','Required parameter body was null or undefined when calling createItemApiV1ItemsPost.');
            }
            const localVarPath = `/api/v1/items/`;
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, 'https://example.com');
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }
            const localVarRequestOptions = { method: 'POST', ...baseOptions, ...options};
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;

            // authentication OAuth2PasswordBearer required
            // oauth required
            if (configuration && configuration.accessToken) {
                const localVarAccessTokenValue = typeof configuration.accessToken === 'function'
                    ? await configuration.accessToken("OAuth2PasswordBearer", [""])
                    : await configuration.accessToken;
                localVarHeaderParameter["Authorization"] = "Bearer " + localVarAccessTokenValue;
            }

            localVarHeaderParameter['Content-Type'] = 'application/json';

            const query = new URLSearchParams(localVarUrlObj.search);
            for (const key in localVarQueryParameter) {
                query.set(key, localVarQueryParameter[key]);
            }
            for (const key in options.query) {
                query.set(key, options.query[key]);
            }
            localVarUrlObj.search = (new URLSearchParams(query)).toString();
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = {...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers};
            const needsSerialization = (typeof body !== "string") || localVarRequestOptions.headers['Content-Type'] === 'application/json';
            localVarRequestOptions.data =  needsSerialization ? JSON.stringify(body !== undefined ? body : {}) : (body || "");

            return {
                url: localVarUrlObj.pathname + localVarUrlObj.search + localVarUrlObj.hash,
                options: localVarRequestOptions,
            };
        },
        /**
         * Delete an item.
         * @summary Delete Item
         * @param {number} id 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        deleteItemApiV1ItemsIdDelete: async (id: number, options: any = {}): Promise<RequestArgs> => {
            // verify required parameter 'id' is not null or undefined
            if (id === null || id === undefined) {
                throw new RequiredError('id','Required parameter id was null or undefined when calling deleteItemApiV1ItemsIdDelete.');
            }
            const localVarPath = `/api/v1/items/{id}`
                .replace(`{${"id"}}`, encodeURIComponent(String(id)));
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, 'https://example.com');
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }
            const localVarRequestOptions = { method: 'DELETE', ...baseOptions, ...options};
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;

            // authentication OAuth2PasswordBearer required
            // oauth required
            if (configuration && configuration.accessToken) {
                const localVarAccessTokenValue = typeof configuration.accessToken === 'function'
                    ? await configuration.accessToken("OAuth2PasswordBearer", [""])
                    : await configuration.accessToken;
                localVarHeaderParameter["Authorization"] = "Bearer " + localVarAccessTokenValue;
            }

            const query = new URLSearchParams(localVarUrlObj.search);
            for (const key in localVarQueryParameter) {
                query.set(key, localVarQueryParameter[key]);
            }
            for (const key in options.query) {
                query.set(key, options.query[key]);
            }
            localVarUrlObj.search = (new URLSearchParams(query)).toString();
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = {...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers};

            return {
                url: localVarUrlObj.pathname + localVarUrlObj.search + localVarUrlObj.hash,
                options: localVarRequestOptions,
            };
        },
        /**
         * Get item by ID.
         * @summary Read Item
         * @param {number} id 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        readItemApiV1ItemsIdGet: async (id: number, options: any = {}): Promise<RequestArgs> => {
            // verify required parameter 'id' is not null or undefined
            if (id === null || id === undefined) {
                throw new RequiredError('id','Required parameter id was null or undefined when calling readItemApiV1ItemsIdGet.');
            }
            const localVarPath = `/api/v1/items/{id}`
                .replace(`{${"id"}}`, encodeURIComponent(String(id)));
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, 'https://example.com');
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }
            const localVarRequestOptions = { method: 'GET', ...baseOptions, ...options};
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;

            // authentication OAuth2PasswordBearer required
            // oauth required
            if (configuration && configuration.accessToken) {
                const localVarAccessTokenValue = typeof configuration.accessToken === 'function'
                    ? await configuration.accessToken("OAuth2PasswordBearer", [""])
                    : await configuration.accessToken;
                localVarHeaderParameter["Authorization"] = "Bearer " + localVarAccessTokenValue;
            }

            const query = new URLSearchParams(localVarUrlObj.search);
            for (const key in localVarQueryParameter) {
                query.set(key, localVarQueryParameter[key]);
            }
            for (const key in options.query) {
                query.set(key, options.query[key]);
            }
            localVarUrlObj.search = (new URLSearchParams(query)).toString();
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = {...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers};

            return {
                url: localVarUrlObj.pathname + localVarUrlObj.search + localVarUrlObj.hash,
                options: localVarRequestOptions,
            };
        },
        /**
         * Retrieve items.
         * @summary Read Items
         * @param {number} [skip] 
         * @param {number} [limit] 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        readItemsApiV1ItemsGet: async (skip?: number, limit?: number, options: any = {}): Promise<RequestArgs> => {
            const localVarPath = `/api/v1/items/`;
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, 'https://example.com');
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }
            const localVarRequestOptions = { method: 'GET', ...baseOptions, ...options};
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;

            // authentication OAuth2PasswordBearer required
            // oauth required
            if (configuration && configuration.accessToken) {
                const localVarAccessTokenValue = typeof configuration.accessToken === 'function'
                    ? await configuration.accessToken("OAuth2PasswordBearer", [""])
                    : await configuration.accessToken;
                localVarHeaderParameter["Authorization"] = "Bearer " + localVarAccessTokenValue;
            }

            if (skip !== undefined) {
                localVarQueryParameter['skip'] = skip;
            }

            if (limit !== undefined) {
                localVarQueryParameter['limit'] = limit;
            }

            const query = new URLSearchParams(localVarUrlObj.search);
            for (const key in localVarQueryParameter) {
                query.set(key, localVarQueryParameter[key]);
            }
            for (const key in options.query) {
                query.set(key, options.query[key]);
            }
            localVarUrlObj.search = (new URLSearchParams(query)).toString();
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = {...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers};

            return {
                url: localVarUrlObj.pathname + localVarUrlObj.search + localVarUrlObj.hash,
                options: localVarRequestOptions,
            };
        },
        /**
         * Update an item.
         * @summary Update Item
         * @param {ItemUpdate} body 
         * @param {number} id 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        updateItemApiV1ItemsIdPut: async (body: ItemUpdate, id: number, options: any = {}): Promise<RequestArgs> => {
            // verify required parameter 'body' is not null or undefined
            if (body === null || body === undefined) {
                throw new RequiredError('body','Required parameter body was null or undefined when calling updateItemApiV1ItemsIdPut.');
            }
            // verify required parameter 'id' is not null or undefined
            if (id === null || id === undefined) {
                throw new RequiredError('id','Required parameter id was null or undefined when calling updateItemApiV1ItemsIdPut.');
            }
            const localVarPath = `/api/v1/items/{id}`
                .replace(`{${"id"}}`, encodeURIComponent(String(id)));
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, 'https://example.com');
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }
            const localVarRequestOptions = { method: 'PUT', ...baseOptions, ...options};
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;

            // authentication OAuth2PasswordBearer required
            // oauth required
            if (configuration && configuration.accessToken) {
                const localVarAccessTokenValue = typeof configuration.accessToken === 'function'
                    ? await configuration.accessToken("OAuth2PasswordBearer", [""])
                    : await configuration.accessToken;
                localVarHeaderParameter["Authorization"] = "Bearer " + localVarAccessTokenValue;
            }

            localVarHeaderParameter['Content-Type'] = 'application/json';

            const query = new URLSearchParams(localVarUrlObj.search);
            for (const key in localVarQueryParameter) {
                query.set(key, localVarQueryParameter[key]);
            }
            for (const key in options.query) {
                query.set(key, options.query[key]);
            }
            localVarUrlObj.search = (new URLSearchParams(query)).toString();
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = {...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers};
            const needsSerialization = (typeof body !== "string") || localVarRequestOptions.headers['Content-Type'] === 'application/json';
            localVarRequestOptions.data =  needsSerialization ? JSON.stringify(body !== undefined ? body : {}) : (body || "");

            return {
                url: localVarUrlObj.pathname + localVarUrlObj.search + localVarUrlObj.hash,
                options: localVarRequestOptions,
            };
        },
    }
};

/**
 * ItemsApi - functional programming interface
 * @export
 */
export const ItemsApiFp = function(configuration?: Configuration) {
    return {
        /**
         * Create new item.
         * @summary Create Item
         * @param {ItemCreate} body 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async createItemApiV1ItemsPost(body: ItemCreate, options?: any): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<Item>> {
            const localVarAxiosArgs = await ItemsApiAxiosParamCreator(configuration).createItemApiV1ItemsPost(body, options);
            return (axios: AxiosInstance = globalAxios, basePath: string = BASE_PATH) => {
                const axiosRequestArgs = {...localVarAxiosArgs.options, url: basePath + localVarAxiosArgs.url};
                return axios.request(axiosRequestArgs);
            };
        },
        /**
         * Delete an item.
         * @summary Delete Item
         * @param {number} id 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async deleteItemApiV1ItemsIdDelete(id: number, options?: any): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<Item>> {
            const localVarAxiosArgs = await ItemsApiAxiosParamCreator(configuration).deleteItemApiV1ItemsIdDelete(id, options);
            return (axios: AxiosInstance = globalAxios, basePath: string = BASE_PATH) => {
                const axiosRequestArgs = {...localVarAxiosArgs.options, url: basePath + localVarAxiosArgs.url};
                return axios.request(axiosRequestArgs);
            };
        },
        /**
         * Get item by ID.
         * @summary Read Item
         * @param {number} id 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async readItemApiV1ItemsIdGet(id: number, options?: any): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<Item>> {
            const localVarAxiosArgs = await ItemsApiAxiosParamCreator(configuration).readItemApiV1ItemsIdGet(id, options);
            return (axios: AxiosInstance = globalAxios, basePath: string = BASE_PATH) => {
                const axiosRequestArgs = {...localVarAxiosArgs.options, url: basePath + localVarAxiosArgs.url};
                return axios.request(axiosRequestArgs);
            };
        },
        /**
         * Retrieve items.
         * @summary Read Items
         * @param {number} [skip] 
         * @param {number} [limit] 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async readItemsApiV1ItemsGet(skip?: number, limit?: number, options?: any): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<Array<Item>>> {
            const localVarAxiosArgs = await ItemsApiAxiosParamCreator(configuration).readItemsApiV1ItemsGet(skip, limit, options);
            return (axios: AxiosInstance = globalAxios, basePath: string = BASE_PATH) => {
                const axiosRequestArgs = {...localVarAxiosArgs.options, url: basePath + localVarAxiosArgs.url};
                return axios.request(axiosRequestArgs);
            };
        },
        /**
         * Update an item.
         * @summary Update Item
         * @param {ItemUpdate} body 
         * @param {number} id 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async updateItemApiV1ItemsIdPut(body: ItemUpdate, id: number, options?: any): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<Item>> {
            const localVarAxiosArgs = await ItemsApiAxiosParamCreator(configuration).updateItemApiV1ItemsIdPut(body, id, options);
            return (axios: AxiosInstance = globalAxios, basePath: string = BASE_PATH) => {
                const axiosRequestArgs = {...localVarAxiosArgs.options, url: basePath + localVarAxiosArgs.url};
                return axios.request(axiosRequestArgs);
            };
        },
    }
};

/**
 * ItemsApi - factory interface
 * @export
 */
export const ItemsApiFactory = function (configuration?: Configuration, basePath?: string, axios?: AxiosInstance) {
    return {
        /**
         * Create new item.
         * @summary Create Item
         * @param {ItemCreate} body 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        createItemApiV1ItemsPost(body: ItemCreate, options?: any): AxiosPromise<Item> {
            return ItemsApiFp(configuration).createItemApiV1ItemsPost(body, options).then((request) => request(axios, basePath));
        },
        /**
         * Delete an item.
         * @summary Delete Item
         * @param {number} id 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        deleteItemApiV1ItemsIdDelete(id: number, options?: any): AxiosPromise<Item> {
            return ItemsApiFp(configuration).deleteItemApiV1ItemsIdDelete(id, options).then((request) => request(axios, basePath));
        },
        /**
         * Get item by ID.
         * @summary Read Item
         * @param {number} id 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        readItemApiV1ItemsIdGet(id: number, options?: any): AxiosPromise<Item> {
            return ItemsApiFp(configuration).readItemApiV1ItemsIdGet(id, options).then((request) => request(axios, basePath));
        },
        /**
         * Retrieve items.
         * @summary Read Items
         * @param {number} [skip] 
         * @param {number} [limit] 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        readItemsApiV1ItemsGet(skip?: number, limit?: number, options?: any): AxiosPromise<Array<Item>> {
            return ItemsApiFp(configuration).readItemsApiV1ItemsGet(skip, limit, options).then((request) => request(axios, basePath));
        },
        /**
         * Update an item.
         * @summary Update Item
         * @param {ItemUpdate} body 
         * @param {number} id 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        updateItemApiV1ItemsIdPut(body: ItemUpdate, id: number, options?: any): AxiosPromise<Item> {
            return ItemsApiFp(configuration).updateItemApiV1ItemsIdPut(body, id, options).then((request) => request(axios, basePath));
        },
    };
};

/**
 * ItemsApi - object-oriented interface
 * @export
 * @class ItemsApi
 * @extends {BaseAPI}
 */
export class ItemsApi extends BaseAPI {
    /**
     * Create new item.
     * @summary Create Item
     * @param {ItemCreate} body 
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof ItemsApi
     */
    public createItemApiV1ItemsPost(body: ItemCreate, options?: any) {
        return ItemsApiFp(this.configuration).createItemApiV1ItemsPost(body, options).then((request) => request(this.axios, this.basePath));
    }
    /**
     * Delete an item.
     * @summary Delete Item
     * @param {number} id 
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof ItemsApi
     */
    public deleteItemApiV1ItemsIdDelete(id: number, options?: any) {
        return ItemsApiFp(this.configuration).deleteItemApiV1ItemsIdDelete(id, options).then((request) => request(this.axios, this.basePath));
    }
    /**
     * Get item by ID.
     * @summary Read Item
     * @param {number} id 
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof ItemsApi
     */
    public readItemApiV1ItemsIdGet(id: number, options?: any) {
        return ItemsApiFp(this.configuration).readItemApiV1ItemsIdGet(id, options).then((request) => request(this.axios, this.basePath));
    }
    /**
     * Retrieve items.
     * @summary Read Items
     * @param {number} [skip] 
     * @param {number} [limit] 
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof ItemsApi
     */
    public readItemsApiV1ItemsGet(skip?: number, limit?: number, options?: any) {
        return ItemsApiFp(this.configuration).readItemsApiV1ItemsGet(skip, limit, options).then((request) => request(this.axios, this.basePath));
    }
    /**
     * Update an item.
     * @summary Update Item
     * @param {ItemUpdate} body 
     * @param {number} id 
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof ItemsApi
     */
    public updateItemApiV1ItemsIdPut(body: ItemUpdate, id: number, options?: any) {
        return ItemsApiFp(this.configuration).updateItemApiV1ItemsIdPut(body, id, options).then((request) => request(this.axios, this.basePath));
    }
}